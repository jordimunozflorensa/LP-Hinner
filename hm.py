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

@dataclass
class Var:
    name: str

@dataclass
class App:
    esq: Type
    dre: Type

@dataclass
class Const:
    value: str

Type = Const | App | Var

taula_de_simbols = {}
file_path = 'data.pkl'

class Buit:
    pass

@dataclass
class Node:
    val: str
    tipus: Type
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

def inserta_tipus(llista: List[str]) -> Type:
    if not llista:
        raise ValueError("La llista no pot ser buida")
    
    result = Const(llista[-1])
    
    for value in reversed(llista[:-1]):
        result = App(Const(value), result)
    
    return result

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
            llista = []
            llista.append(type_var)
            for i in range(0, len(types), 2):
                llista.append(types[i-1].getText())
            
            taula_de_simbols[var.getText()] = inserta_tipus(llista)
            # print(llista)
            # taula_de_simbols[var.getText()] = Const("hola")
        else:
            taula_de_simbols[var.getText()] = Const(type_var)
        save_data()

    def visitApp(self, ctx):
        [expr1, expr2] = list(ctx.getChildren())
        left = self.visit(expr1)
        right = self.visit(expr2)
        e = Node('@', Var(self.lletra), left, right)
        self.lletra = chr(ord(self.lletra) + 1)
        return e

    def visitLambda(self, ctx):
        [_, id_, _, expr] = list(ctx.getChildren())
        if id_.getText() in taula_de_simbols:
            param = Node(id_.getText(), taula_de_simbols[id_.getText()], Buit(), Buit())
        else:
            if id_.getText() not in self.variables:
                self.variables[id_.getText()] = Var(self.lletra)
                self.lletra = chr(ord(self.lletra) + 1)
            param = Node(id_.getText(), self.variables[id_.getText()], Buit(), Buit())
        body = self.visit(expr)
        e = Node('λ', Var(self.lletra), param, body)
        self.lletra = chr(ord(self.lletra) + 1)
        return e
    
    def visitOper(self, ctx):
        [oper] = list(ctx.getChildren())
        if oper.getText() in taula_de_simbols:
            e = Node(oper.getText(), taula_de_simbols[oper.getText()], Buit(), Buit())
        else:
            if oper.getText() not in self.variables:
                self.variables[oper.getText()] = Var(self.lletra)
                self.lletra = chr(ord(self.lletra) + 1)
            e = Node(oper.getText(), self.variables[oper.getText()], Buit(), Buit())
        return e

    def visitIdexpr(self, ctx):
        [id_] = list(ctx.getChildren())
        if id_.getText() in taula_de_simbols:
            e = Node(id_.getText(), taula_de_simbols[id_.getText()], Buit(), Buit())
        else:
            if id_.getText() not in self.variables:
                self.variables[id_.getText()] = Var(self.lletra)
                self.lletra = chr(ord(self.lletra) + 1)
            e = Node(id_.getText(), self.variables[id_.getText()], Buit(), Buit())
        return e
    
    def visitNumexpr(self, ctx):
        [num] = list(ctx.getChildren())
        if num.getText() in taula_de_simbols:
            e = Node(num.getText(), taula_de_simbols[num.getText()], Buit(), Buit())
        else:
            if num.getText() not in self.variables:
                self.variables[num.getText()] = Var(self.lletra)
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


def showtype(t: Type) -> str:
    if isinstance(t, Var):
        return t.name
    elif isinstance(t, Const):
        return t.value
    elif isinstance(t, App):
        return f"{showtype(t.name)}({showtype(t.args)})"
    return ""


def parseja_tipus(tipus: Type) -> str:
    if isinstance(tipus, Const):
        return tipus.value
    elif isinstance(tipus, Var):
        return tipus.name
    elif isinstance(tipus, App):
        esq_str = parseja_tipus(tipus.esq)
        dre_str = parseja_tipus(tipus.dre)
        return f"({esq_str} -> {dre_str})"
    else:
        raise TypeError("Type no acceptat al parsejar un tipus")


def to_dot(arbre: Arbre, graph=None, parent=None, node_id=0):
    if graph is None:
        graph = Graph()
    
    if isinstance(arbre, Buit):
        return graph, node_id
    
    node_label = arbre.val + '\n' + parseja_tipus(arbre.tipus)

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
        pickle.dump(taula_de_simbols, f)
    
def load_data():
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


taula_de_simbols = load_data()

st.title("Inferència de tipus")
msg = st.text_area(label='Expressió:', value='(+) :: N -> N -> N\n2 :: N\n\\x -> (+) 2 x', height=50)

if st.button('fer'):
    input_stream =  InputStream(msg)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    visitor.visit(tree)
    # print(res)

    st.write(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')

    d = taula_de_simbols
    data = [(var, parseja_tipus(tipus)) for var, tipus in d.items()]
    df = pd.DataFrame(data, columns=['Var', 'Tipus'])
    st.dataframe(df)

if st.button('resetejar'):
    taula_de_simbols = {}
    save_data()


# def unify(x, y, subst):
#     """Unifies term x and y with initial subst.

#     Returns a subst (map of name->term) that unifies x and y, or None if
#     they can't be unified. Pass subst={} if no subst are initially
#     known. Note that {} means valid (but empty) subst.
#     """
#     if subst is None:
#         return None
#     elif x == y:
#         return subst
#     elif isinstance(x, Var):
#         return unify_variable(x, y, subst)
#     elif isinstance(y, Var):
#         return unify_variable(y, x, subst)
#     elif isinstance(x, App) and isinstance(y, App):
#         if x.fname != y.fname or len(x.args) != len(y.args):
#             return None
#         else:
#             for i in range(len(x.args)):
#                 subst = unify(x.args[i], y.args[i], subst)
#             return subst
#     else:
#         return None


# def unify_variable(v, x, subst):
#     """Unifies variable v with term x, using subst.

#     Returns updated subst or None on failure.
#     """
#     assert isinstance(v, Var)
#     if v.name in subst:
#         return unify(subst[v.name], x, subst)
#     elif isinstance(x, Var) and x.name in subst:
#         return unify(v, subst[x.name], subst)
#     elif occurs_check(v, x, subst):
#         return None
#     else:
#         # v is not yet in subst and can't simplify x. Extend subst.
#         return {**subst, v.name: x}


# def occurs_check(v, term, subst):
#     """Does the variable v occur anywhere inside term?

#     Variables in term are looked up in subst and the check is applied
#     recursively.
#     """
#     assert isinstance(v, Var)
#     if v == term:
#         return True
#     elif isinstance(term, Var) and term.name in subst:
#         return occurs_check(v, subst[term.name], subst)
#     elif isinstance(term, App):
#         return any(occurs_check(v, arg, subst) for arg in term.args)
#     else:
#         return False