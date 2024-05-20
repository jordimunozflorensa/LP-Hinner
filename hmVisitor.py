# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#typing.
    def visitTyping(self, ctx:hmParser.TypingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#app.
    def visitApp(self, ctx:hmParser.AppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#paren.
    def visitParen(self, ctx:hmParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#lambda.
    def visitLambda(self, ctx:hmParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#oper.
    def visitOper(self, ctx:hmParser.OperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#idexpr.
    def visitIdexpr(self, ctx:hmParser.IdexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#numexpr.
    def visitNumexpr(self, ctx:hmParser.NumexprContext):
        return self.visitChildren(ctx)



del hmParser