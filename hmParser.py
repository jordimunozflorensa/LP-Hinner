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
        4,1,10,55,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,3,0,14,8,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,5,1,29,8,1,10,1,12,1,32,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,
        9,2,1,2,0,1,4,3,0,2,4,0,1,2,0,1,1,9,9,60,0,9,1,0,0,0,2,23,1,0,0,
        0,4,45,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,
        9,10,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,12,14,3,4,2,0,13,12,1,0,
        0,0,13,14,1,0,0,0,14,18,1,0,0,0,15,17,3,2,1,0,16,15,1,0,0,0,17,20,
        1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,
        21,22,5,0,0,1,22,1,1,0,0,0,23,24,7,0,0,0,24,25,5,6,0,0,25,30,5,8,
        0,0,26,27,5,4,0,0,27,29,5,8,0,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,
        1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,0,32,30,1,0,0,0,33,34,6,2,-1,0,
        34,35,5,2,0,0,35,36,3,4,2,0,36,37,5,3,0,0,37,46,1,0,0,0,38,39,5,
        5,0,0,39,40,5,7,0,0,40,41,5,4,0,0,41,46,3,4,2,4,42,46,5,1,0,0,43,
        46,5,7,0,0,44,46,5,9,0,0,45,33,1,0,0,0,45,38,1,0,0,0,45,42,1,0,0,
        0,45,43,1,0,0,0,45,44,1,0,0,0,46,51,1,0,0,0,47,48,10,5,0,0,48,50,
        3,4,2,6,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,
        52,5,1,0,0,0,53,51,1,0,0,0,6,9,13,18,30,45,51
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'->'", "'\\'", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "OPER", "LPAR", "RPAR", "ARROW", "CBAR", 
                      "PP", "ID", "TYPE", "NUM", "WS" ]

    RULE_root = 0
    RULE_typing = 1
    RULE_expr = 2

    ruleNames =  [ "root", "typing", "expr" ]

    EOF = Token.EOF
    OPER=1
    LPAR=2
    RPAR=3
    ARROW=4
    CBAR=5
    PP=6
    ID=7
    TYPE=8
    NUM=9
    WS=10

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

        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

        def typing(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TypingContext)
            else:
                return self.getTypedRuleContext(hmParser.TypingContext,i)


        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 6
                    self.typing() 
                self.state = 11
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 13
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 12
                self.expr(0)


            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==9:
                self.state = 15
                self.typing()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(hmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PP(self):
            return self.getToken(hmParser.PP, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.TYPE)
            else:
                return self.getToken(hmParser.TYPE, i)

        def OPER(self):
            return self.getToken(hmParser.OPER, 0)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.ARROW)
            else:
                return self.getToken(hmParser.ARROW, i)

        def getRuleIndex(self):
            return hmParser.RULE_typing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyping" ):
                return visitor.visitTyping(self)
            else:
                return visitor.visitChildren(self)




    def typing(self):

        localctx = hmParser.TypingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==1 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 24
            self.match(hmParser.PP)
            self.state = 25
            self.match(hmParser.TYPE)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 26
                self.match(hmParser.ARROW)
                self.state = 27
                self.match(hmParser.TYPE)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AppContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp" ):
                return visitor.visitApp(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(hmParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(hmParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class LambdaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CBAR(self):
            return self.getToken(hmParser.CBAR, 0)
        def ID(self):
            return self.getToken(hmParser.ID, 0)
        def ARROW(self):
            return self.getToken(hmParser.ARROW, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambda" ):
                return visitor.visitLambda(self)
            else:
                return visitor.visitChildren(self)


    class OperContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPER(self):
            return self.getToken(hmParser.OPER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOper" ):
                return visitor.visitOper(self)
            else:
                return visitor.visitChildren(self)


    class IdexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdexpr" ):
                return visitor.visitIdexpr(self)
            else:
                return visitor.visitChildren(self)


    class NumexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumexpr" ):
                return visitor.visitNumexpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = hmParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 34
                self.match(hmParser.LPAR)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(hmParser.RPAR)
                pass
            elif token in [5]:
                localctx = hmParser.LambdaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(hmParser.CBAR)
                self.state = 39
                self.match(hmParser.ID)
                self.state = 40
                self.match(hmParser.ARROW)
                self.state = 41
                self.expr(4)
                pass
            elif token in [1]:
                localctx = hmParser.OperContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(hmParser.OPER)
                pass
            elif token in [7]:
                localctx = hmParser.IdexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(hmParser.ID)
                pass
            elif token in [9]:
                localctx = hmParser.NumexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(hmParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AppContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 47
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 48
                    self.expr(6) 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




