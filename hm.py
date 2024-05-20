from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
import streamlit as st
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
import pickle
from typing import Tuple, List, Dict, Union
from graphviz import Graph
import pandas as pd

estat_global = {}
file_path = 'data.pkl'

class Buit:
    pass

@dataclass
class Node:
    val: str
    tipus: str
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

class TreeVisitor(hmVisitor):
    def __init__(self):
        self.lletra = 'a'
        self.variables = {}

    def visitRoot(self, ctx):
        resultats = []
        for expressio in ctx.getChildren():
            e = self.visit(expressio)
            if e is not None:
                graphviz_chart(e)
            resultats.append(e)
        return resultats
        
    def visitParen(self, ctx):
        [_, expr, _] = list(ctx.getChildren())
        e = self.visit(expr)
        return e

    def visitTyping(self, ctx):
        [var, _, type_, *types] = list(ctx.getChildren())
        type_var = type_.getText()
        if len(types) != 0:
            for i in range(0, len(types), 2):
                if i == 0:
                    type_var = "(" + type_var
                else:
                    type_var = type_var + types[i].getText() + "(" + types[i+1].getText()
            type_var = type_var + types[-2].getText() + types[-1].getText()
            for i in range(len(types) // 2):
                type_var = type_var + ")"
        estat_global[var.getText()] = type_var
        save_data()

    def visitApp(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        left = self.visit(expr1)
        right = self.visit(expr2)
        e = Node('@', self.lletra, left, right)
        self.lletra = chr(ord(self.lletra) + 1)
        return e

    def visitLambda(self, ctx):
        [_, id_, _, expr] = list(ctx.getChildren())
        if id_.getText() in estat_global:
            param = Node(id_.getText(), estat_global[id_.getText()], Buit(), Buit())
        else:
            if id_.getText() not in self.variables:
                self.variables[id_.getText()] = self.lletra
                self.lletra = chr(ord(self.lletra) + 1)
            param = Node(id_.getText(), self.variables[id_.getText()], Buit(), Buit())
        body = self.visit(expr)
        e = Node('λ', self.lletra, param, body)
        self.lletra = chr(ord(self.lletra) + 1)
        return e
    
    def visitOper(self, ctx):
        [oper] = list(ctx.getChildren())
        if oper.getText() in estat_global:
            e = Node(oper.getText(), estat_global[oper.getText()], Buit(), Buit())
        else:
            if oper.getText() not in self.variables:
                self.variables[oper.getText()] = self.lletra
                self.lletra = chr(ord(self.lletra) + 1)
            e = Node(oper.getText(), self.variables[oper.getText()], Buit(), Buit())
        return e

    def visitIdexpr(self, ctx):
        [id_] = list(ctx.getChildren())
        if id_.getText() in estat_global:
            e = Node(id_.getText(), estat_global[id_.getText()], Buit(), Buit())
        else:
            if id_.getText() not in self.variables:
                self.variables[id_.getText()] = self.lletra
                self.lletra = chr(ord(self.lletra) + 1)
            e = Node(id_.getText(), self.variables[id_.getText()], Buit(), Buit())
        return e
    
    def visitNumexpr(self, ctx):
        [num] = list(ctx.getChildren())
        if num.getText() in estat_global:
            e = Node(num.getText(), estat_global[num.getText()], Buit(), Buit())
        else:
            if num.getText() not in self.variables:
                self.variables[num.getText()] = self.lletra
                self.lletra = chr(ord(self.lletra) + 1)
            e = Node(num.getText(), self.variables[num.getText()], Buit(), Buit())
        return e


def print_arbre(arbre: Arbre, level=0):
    if isinstance(arbre, Buit):
        print(" " * (level * 2) + "Buit")
    elif isinstance(arbre, Node):
        print(" " * (level * 2) + arbre.val)
        print_arbre(arbre.esq, level + 1)
        print_arbre(arbre.dre, level + 1)


def to_dot(arbre: Arbre, graph=None, parent=None, node_id=0):
    if graph is None:
        graph = Graph()
    
    if isinstance(arbre, Buit):
        return graph, node_id
    
    node_label = arbre.val + '\n' + arbre.tipus

    current_node_id = f'node{node_id}'
    graph.node(current_node_id, node_label)
    
    if parent is not None:
        graph.edge(parent, current_node_id)
    
    node_id += 1
    
    if isinstance(arbre, Node):
        graph, node_id = to_dot(arbre.esq, graph, current_node_id, node_id)
        graph, node_id = to_dot(arbre.dre, graph, current_node_id, node_id)
    
    return graph, node_id

def graphviz_chart(arbre: Arbre):
    dot, _ = to_dot(arbre)
    st.graphviz_chart(dot)

def save_data():
    with open(file_path, 'wb') as f:
        pickle.dump(estat_global, f)
    
def load_data():
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


estat_global = load_data()

st.title("Inferència de tipus")
msg = st.text_area(label='Expressió:', value='\\x -> (+) 2 x', height=50)

if st.button('fer'):
    input_stream =  InputStream(msg)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    visitor.visit(tree)

    st.write(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')

    d = estat_global
    data = [(var, tipus) for var, tipus in d.items()]
    df = pd.DataFrame(data, columns=['Var', 'Tipus'])
    st.dataframe(df)

if st.button('resetejar'):
    estat_global = {}
    save_data()