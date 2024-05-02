# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,4,1,18,8,1,11,1,12,1,19,1,2,1,2,1,2,3,2,25,8,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,42,8,
        3,1,4,1,4,1,4,1,4,1,4,5,4,49,8,4,10,4,12,4,52,9,4,1,5,1,5,1,5,1,
        5,1,5,1,5,3,5,60,8,5,1,6,1,6,1,6,0,1,8,7,0,2,4,6,8,10,12,0,1,1,0,
        1,4,64,0,14,1,0,0,0,2,17,1,0,0,0,4,24,1,0,0,0,6,41,1,0,0,0,8,43,
        1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,
        18,3,4,2,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,3,1,0,0,0,21,25,3,10,5,0,22,25,3,8,4,0,23,25,3,6,3,0,24,21,
        1,0,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,5,1,0,0,0,26,27,5,8,0,0,27,
        28,5,9,0,0,28,29,5,7,0,0,29,30,3,10,5,0,30,31,3,10,5,0,31,32,3,10,
        5,0,32,42,1,0,0,0,33,34,5,5,0,0,34,35,3,6,3,0,35,36,5,6,0,0,36,42,
        1,0,0,0,37,38,5,5,0,0,38,39,3,12,6,0,39,40,5,6,0,0,40,42,1,0,0,0,
        41,26,1,0,0,0,41,33,1,0,0,0,41,37,1,0,0,0,42,7,1,0,0,0,43,44,6,4,
        -1,0,44,45,3,6,3,0,45,50,1,0,0,0,46,47,10,2,0,0,47,49,3,10,5,0,48,
        46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,1,0,0,
        0,52,50,1,0,0,0,53,60,5,9,0,0,54,60,5,10,0,0,55,56,5,5,0,0,56,57,
        3,10,5,0,57,58,5,6,0,0,58,60,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,0,
        59,55,1,0,0,0,60,11,1,0,0,0,61,62,7,0,0,0,62,13,1,0,0,0,5,19,24,
        41,50,59
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'->'", "'\\'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "LPAR", 
                      "RPAR", "ARROW", "CBAR", "ID", "NUM", "WS" ]

    RULE_root = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_lam = 3
    RULE_apl = 4
    RULE_expr = 5
    RULE_oper = 6

    ruleNames =  [ "root", "stmts", "stmt", "lam", "apl", "expr", "oper" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    LPAR=5
    RPAR=6
    ARROW=7
    CBAR=8
    ID=9
    NUM=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(hmParser.StmtsContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.StmtContext)
            else:
                return self.getTypedRuleContext(hmParser.StmtContext,i)


        def getRuleIndex(self):
            return hmParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = hmParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stmt()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1824) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def apl(self):
            return self.getTypedRuleContext(hmParser.AplContext,0)


        def lam(self):
            return self.getTypedRuleContext(hmParser.LamContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = hmParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.apl(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.lam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CBAR(self):
            return self.getToken(hmParser.CBAR, 0)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)

        def lam(self):
            return self.getTypedRuleContext(hmParser.LamContext,0)


        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def oper(self):
            return self.getTypedRuleContext(hmParser.OperContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_lam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLam" ):
                return visitor.visitLam(self)
            else:
                return visitor.visitChildren(self)




    def lam(self):

        localctx = hmParser.LamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lam)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(hmParser.CBAR)
                self.state = 27
                self.match(hmParser.ID)
                self.state = 28
                self.match(hmParser.ARROW)
                self.state = 29
                self.expr()
                self.state = 30
                self.expr()
                self.state = 31
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(hmParser.LPAR)
                self.state = 34
                self.lam()
                self.state = 35
                self.match(hmParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(hmParser.LPAR)
                self.state = 38
                self.oper()
                self.state = 39
                self.match(hmParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AplContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lam(self):
            return self.getTypedRuleContext(hmParser.LamContext,0)


        def apl(self):
            return self.getTypedRuleContext(hmParser.AplContext,0)


        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_apl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApl" ):
                return visitor.visitApl(self)
            else:
                return visitor.visitChildren(self)



    def apl(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.AplContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_apl, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.lam()
            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_apl)
                    self.state = 46
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 47
                    self.expr() 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def getRuleIndex(self):
            return hmParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = hmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(hmParser.ID)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(hmParser.NUM)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(hmParser.LPAR)
                self.state = 56
                self.expr()
                self.state = 57
                self.match(hmParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(hmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(hmParser.MINUS, 0)

        def MUL(self):
            return self.getToken(hmParser.MUL, 0)

        def DIV(self):
            return self.getToken(hmParser.DIV, 0)

        def getRuleIndex(self):
            return hmParser.RULE_oper

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOper" ):
                return visitor.visitOper(self)
            else:
                return visitor.visitChildren(self)




    def oper(self):

        localctx = hmParser.OperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_oper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.apl_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def apl_sempred(self, localctx:AplContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




