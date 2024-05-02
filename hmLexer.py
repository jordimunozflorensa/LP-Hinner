# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,4,8,42,8,8,11,8,
        12,8,43,1,9,4,9,47,8,9,11,9,12,9,48,1,10,4,10,52,8,10,11,10,12,10,
        53,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,
        21,11,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,59,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,
        0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,
        0,0,0,13,35,1,0,0,0,15,38,1,0,0,0,17,41,1,0,0,0,19,46,1,0,0,0,21,
        51,1,0,0,0,23,24,5,43,0,0,24,2,1,0,0,0,25,26,5,45,0,0,26,4,1,0,0,
        0,27,28,5,42,0,0,28,6,1,0,0,0,29,30,5,47,0,0,30,8,1,0,0,0,31,32,
        5,40,0,0,32,10,1,0,0,0,33,34,5,41,0,0,34,12,1,0,0,0,35,36,5,45,0,
        0,36,37,5,62,0,0,37,14,1,0,0,0,38,39,5,92,0,0,39,16,1,0,0,0,40,42,
        2,97,122,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,18,1,0,0,0,45,47,7,0,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,
        1,0,0,0,48,49,1,0,0,0,49,20,1,0,0,0,50,52,7,1,0,0,51,50,1,0,0,0,
        52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,6,
        10,0,0,56,22,1,0,0,0,4,0,43,48,53,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    LPAR = 5
    RPAR = 6
    ARROW = 7
    CBAR = 8
    ID = 9
    NUM = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'->'", "'\\'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "LPAR", "RPAR", "ARROW", "CBAR", 
            "ID", "NUM", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "LPAR", "RPAR", "ARROW", 
                  "CBAR", "ID", "NUM", "WS" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

