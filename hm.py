from antlr4 import *
import streamlit as st
# from exprsLexer import exprsLexer
# from exprsParser import exprsParser
# from exprsVisitor import exprsVisitor
import sys

st.write('Hello world!')
# class EvalVisitor(exprsVisitor):
  

# if (len(sys.argv) > 1):
#   input_stream = FileStream(sys.argv[1])
# else:
#   input_stream = StdinStream()

# lexer = exprsLexer(input_stream)
# token_stream = CommonTokenStream(lexer)
# parser = exprsParser(token_stream)
# tree = parser.root()

# if parser.getNumberOfSyntaxErrors() == 0:
#   # visitor = TreeVisitor()
#   # visitor.visit(tree)
#   visitor = EvalVisitor()
#   visitor.visit(tree)
# else:
#   print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
#   print(tree.toStringTree(recog=parser))