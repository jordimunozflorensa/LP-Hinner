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
from typing import Tuple, List, Dict
from graphviz import Graph
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
        self.id = 0
        self.dot = Graph()
        self.father = -1
        self.estat = {}
    
    def visitParen(self, ctx):
        [_, expr, _] = list(ctx.getChildren())
        self.visit(expr)

    # (OPER | NUM) PP TYPE (ARROW TYPE)*    # typing
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

        self.estat[var.getText()] = type_var
        

    def visitApp(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        self.dot.node(str(self.id), '@')
        if self.father != -1:
            self.dot.edge(str(self.father), str(self.id))
        self.father = self.id
        var = self.id
        self.id += 1
        self.visit(expr1)
        self.father = var
        self.id += 1
        self.visit(expr2)

    def visitLambda(self, ctx):
        [_, id_, _, expr] = list(ctx.getChildren())
        self.dot.node(str(self.id), 'λ')
        if self.father != -1:
            self.dot.edge(str(self.father), str(self.id))

        self.father = self.id
        self.id += 1

        self.dot.node(str(self.id), id_.getText())
        self.dot.edge(str(self.father), str(self.id))

        self.id += 1
        self.visit(expr)
    
    def visitOper(self, ctx):
        [oper] = list(ctx.getChildren())
        self.dot.node(str(self.id), oper.getText())
        if self.father != -1:
            self.dot.edge(str(self.father), str(self.id))
    
    def visitIdexpr(self, ctx):
        [id_] = list(ctx.getChildren())
        self.dot.node(str(self.id), id_.getText())
        if self.father != -1:
            self.dot.edge(str(self.father), str(self.id))
    
    def visitNumexpr(self, ctx):
        [num] = list(ctx.getChildren())
        self.dot.node(str(self.id), num.getText())
        if self.father != -1:
            self.dot.edge(str(self.father), str(self.id))
    
    def get_dot(self):
        return self.dot

    def get_state(self):
        return self.estat    

class Nothing(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

st.title("Inferencia de tipus")
msg = st.text_area(label='Expressió:', value='\\x -> (+) 2 x', height=50)


# estat = {}
# estat_serialitzat = pickle.dumps(estat)
# estat = pickle.loads(estat_serialitzat)
if st.button('fer'):
    input_stream = InputStream(msg)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    visitor.visit(tree)
    
    dot = visitor.get_dot()
    d = visitor.get_state()
    #st.write(d)
    st.graphviz_chart(dot.source)
    st.write(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')
    data = data = [(var, tipus) for var, tipus in d.items()]
    df = pd.DataFrame(data, columns=['Var', 'Tipus'])
    st.dataframe(df)