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


    # Visit a parse tree produced by hmParser#stmts.
    def visitStmts(self, ctx:hmParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#stmt.
    def visitStmt(self, ctx:hmParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#lam.
    def visitLam(self, ctx:hmParser.LamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#apl.
    def visitApl(self, ctx:hmParser.AplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#expr.
    def visitExpr(self, ctx:hmParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#oper.
    def visitOper(self, ctx:hmParser.OperContext):
        return self.visitChildren(ctx)



del hmParser