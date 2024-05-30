from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
import streamlit as st
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
import pickle
from typing import List
from graphviz import Graph
import pandas as pd

# -----------------------------------------------------------------------------

# TIPUS ALGEBRAICS

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
file_path = 'backup.pkl'

class Buit:
    pass

@dataclass
class Node:
    val: str
    tipus: Type
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

# -----------------------------------------------------------------------------

# FUNCIONS

# Funcio per imprimir l'arbre per terminal, utilizada per debugar
def print_arbre(arbre: Arbre, level=0):
    if isinstance(arbre, Buit):
        print(" " * (level * 2) + "Buit")
    elif isinstance(arbre, Node):
        print(" " * (level * 2) + arbre.val)
        print_arbre(arbre.esq, level + 1)
        print_arbre(arbre.dre, level + 1)

# Funcio per parejar un tipus en format string
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

# Funcio per convertir l'arbre en format dot per a ser visualitzat amb graphviz
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

# Funcio per visualitzar el grafic generat per graphviz
def graphviz_chart(arbre: Arbre):
    dot, _ = to_dot(arbre)
    st.graphviz_chart(dot)

# Funcio per guardar la taula de simbols
def save_data():
    with open(file_path, 'wb') as f:
        pickle.dump(taula_de_simbols, f)
    
# Funcio per carregar la taula de simbols
def load_data():
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

# Funcio per insertar un tipus en format string a l'arbre
def inserta_tipus(llista: List[str]) -> Type:
    if not llista:
        raise ValueError("La llista no pot ser buida")
    
    result = Const(llista[-1])
    
    for value in reversed(llista[:-1]):
        result = App(Const(value), result)
    
    return result

# esq = dre -> @
def infereix_App(arb : Arbre, taula_inferida):
    if isinstance(arb, Buit):
        return
    
    infereix_App(arb.esq, taula_inferida)
    infereix_App(arb.dre, taula_inferida)   

    if isinstance(arb.tipus, Var) and arb.val == '@':
        # Si esq es una App o un Const
        if not isinstance(arb.esq.tipus, Var):
            # Si dre es una App o un Const i no es poden inferir
            if not isinstance(arb.dre.tipus, Var) and (arb.esq.tipus.esq != arb.dre.tipus):
                st.write('TypeError => No es pot inferir el tipus: ' + parseja_tipus(arb.esq.tipus.esq) + ' amb el tipus: ' + parseja_tipus(arb.dre.tipus))
                raise Exception()
            
            # inferir tipus en cas de que no es pugui inferir
            if not isinstance(arb.esq.tipus, Const):
                taula_inferida[arb.tipus.name] = arb.esq.tipus.dre
                if isinstance(arb.dre.tipus, Var):
                    taula_inferida[arb.dre.tipus.name] = arb.esq.tipus.esq
                    arb.dre.tipus = arb.esq.tipus.esq
                arb.tipus = arb.esq.tipus.dre
                
                # Guardar tipus a la taula de simbols
                taula_de_simbols[arb.dre.val] = arb.dre.tipus
                taula_de_simbols[arb.val] = arb.esq.tipus.dre

# λ = esq -> dre
def infereix_Abs(arb : Arbre, taula_inferida):
    if isinstance(arb, Buit):
        return
    
    infereix_Abs(arb.esq, taula_inferida)
    infereix_Abs(arb.dre, taula_inferida)

    if isinstance(arb.tipus, Var) and arb.val == 'λ':
        # Si esq es una App o un Const
        if not isinstance(arb.dre.tipus, Var):
            arb.esq.tipus = taula_de_simbols[arb.esq.val]
            taula_inferida[arb.tipus.name] = App(arb.esq.tipus, arb.dre.tipus)
            arb.tipus = App(arb.esq.tipus, arb.dre.tipus)

# Funcions per escriure una taula a l'streamlit
def escriu_taula(taula):
    t = taula
    data = [(var, parseja_tipus(tipus)) for var, tipus in t.items()]
    df = pd.DataFrame(data, columns=['Var', 'Tipus'])
    st.dataframe(df)

# -----------------------------------------------------------------------------

# TREEVISITOR

# Visitor per recorrer l'arbre
class TreeVisitor(hmVisitor):
    def __init__(self):
        self.lletra = 'a'
        self.variables = {}

    # Funcio per visitar el node root i en cas que sigui una expressió 
    # realitzar les escriptures de les taules i els grafs.
    def visitRoot(self, ctx):
        # variable utilitzada per debuggar
        resultats = []
        for expressio in ctx.getChildren():
            e = self.visit(expressio)
            # en cas de que sigui una expressió
            if e is not None:
                
                escriu_taula(taula_de_simbols)
                graphviz_chart(e)

                # inferencia de tipus
                taula_inferida = {}
                # inferim els tipus aplicació i els tipus abstracció
                infereix_App(e, taula_inferida)
                infereix_Abs(e, taula_inferida)
                
                # en cas de que hi hagi tipus a inferir s'imprimeixen
                if taula_inferida != {}:
                    graphviz_chart(e)
                    escriu_taula(taula_inferida)

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
    
# -----------------------------------------------------------------------------

# GESTIÓ DE STREAMLIT

# Estrucutra de dades per a guardar la taula de simbols
taula_de_simbols = load_data()

st.title("Inferència de tipus")
msg = st.text_area(label='Expressió:', value='(+) :: N -> N -> N\n2 :: M\n\\x -> \\y -> (+) 2 ((+) x y)', height=50)

if st.button('resetejar'):
    taula_de_simbols = {}
    save_data()

if st.button('fer'):
    input_stream =  InputStream(msg)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    if str(parser.getNumberOfSyntaxErrors()) == '0':
        visitor.visit(tree)
    # t_res = visitor.visit(tree)
    # print(t_res)
    # st.write(tree.toStringTree(recog=parser))
    st.write(str(parser.getNumberOfSyntaxErrors()) + ' errors de sintaxi.')

# -----------------------------------------------------------------------------