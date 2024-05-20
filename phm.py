# eli berdensky blog unificacio
# antlr4 -Dlanguage=Python3 -no-listener hm.g4
# antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
# python3 hm.py

from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
import streamlit as st
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
from pickle import dump, load
from typing import Tuple, List, Dict, Union
from graphviz import Digraph
import pandas as pd

class Buit:
    pass

@dataclass
class Node:
    val: str
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

class TreeVisitor(hmVisitor):
    def __init__(self):
        self.root = Buit()
        self.estat = {}
    
    def visitParen(self, ctx):
        [_, expr, _] = list(ctx.getChildren())
        return self.visit(expr)

    # def visitTyping(self, ctx):
    #     [var, _, type_, *types] = list(ctx.getChildren())        
    #     type_var = type_.getText()
        
    #     if len(types) != 0:
    #         for i in range(0, len(types), 2):
    #             if i == 0:
    #                 type_var = "(" + type_var
    #             else:
    #                 type_var = type_var + types[i].getText() + "(" + types[i+1].getText()
            
    #         type_var = type_var + types[-2].getText() + types[-1].getText()

    #         for i in range(len(types) // 2):
    #             type_var = type_var + ")"

    #     self.estat[var.getText()] = type_var

    def visitApp(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        left = self.visit(expr1)
        right = self.visit(expr2)
        return Node('@', left, right)

    def visitLambda(self, ctx):
        [_, id_, _, expr] = list(ctx.getChildren())
        param = Node(id_.getText(), Buit(), Buit())
        body = self.visit(expr)
        return Node('λ', param, body)
    
    def visitOper(self, ctx):
        [oper] = list(ctx.getChildren())
        return Node(oper.getText(), Buit(), Buit())
    
    def visitIdexpr(self, ctx):
        [id_] = list(ctx.getChildren())
        return Node(id_.getText(), Buit(), Buit())
    
    def visitNumexpr(self, ctx):
        [num] = list(ctx.getChildren())
        return Node(num.getText(), Buit(), Buit())
    
    def get_tree(self):
        return self.root

    def get_state(self):
        return self.estat    

def print_arbre(arbre: Arbre, level=0):
    if isinstance(arbre, Buit):
        print(" " * (level * 2) + "Buit")
    elif isinstance(arbre, Node):
        print(" " * (level * 2) + arbre.val)
        print_arbre(arbre.esq, level + 1)
        print_arbre(arbre.dre, level + 1)

# def to_dot(arbre: Arbre, graph=None, parent=None, node_id=0):
#     if graph is None:
#         graph = Digraph()
    
#     if isinstance(arbre, Buit):
#         return graph, node_id
    
#     node_label = arbre.val
#     current_node_id = f'node{node_id}'
#     graph.node(current_node_id, node_label)
    
#     if parent is not None:
#         graph.edge(parent, current_node_id)
    
#     node_id += 1
    
#     if isinstance(arbre, Node):
#         graph, node_id = to_dot(arbre.esq, graph, current_node_id, node_id)
#         graph, node_id = to_dot(arbre.dre, graph, current_node_id, node_id)
    
#     return graph, node_id

# def graphviz_chart(arbre: Arbre):
#     dot, _ = to_dot(arbre)
#     st.graphviz_chart(dot)


st.title("Inferència de tipus")
msg = st.text_area(label='Expressió:', value='\\x -> (+) 2 x', height=50)


if st.button('fer'):
    input_stream = InputStream(msg)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    visitor.root = visitor.visit(tree)
    
    arbre_semantic = visitor.get_tree()
    print_arbre(arbre_semantic)
    d = visitor.get_state()
    
    #graphviz_chart(arbre_semantic)
    st.write(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
    
    data = [(var, tipus) for var, tipus in d.items()]
    df = pd.DataFrame(data, columns=['Var', 'Tipus'])
    st.dataframe(df)