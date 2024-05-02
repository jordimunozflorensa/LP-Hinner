# antlr4 -Dlanguage=Python3 -no-listener hm.g4
# antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
# python3 hm.py
from antlr4 import *
import streamlit as st
from hmLexer import hmLexer
from hmParser import hmParser
# import hmVisitor
# import sys

# if (len(sys.argv) > 1):
#   input_stream = FileStream(sys.argv[1])
# else:
#   input_stream = StdinStream()

input_stream = InputStream(input('? '))
lexer = hmLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = hmParser(token_stream)
tree = parser.root()

st.title('Pràctica 1: Analitzador sintàctic')
st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')ç
st.write("jweirjweo")
print(tree.toStringTree(recog=parser))