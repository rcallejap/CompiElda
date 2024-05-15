# Generated from little_duck.g4 by ANTLR 4.13.0
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
        4,1,34,268,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,0,3,0,79,8,0,1,
        0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,1,0,1,0,1,0,1,1,1,1,4,1,93,8,1,
        11,1,12,1,94,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        109,8,3,10,3,12,3,112,9,3,1,4,3,4,115,8,4,1,5,1,5,1,6,1,6,5,6,121,
        8,6,10,6,12,6,124,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,133,8,7,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,3,10,151,8,10,1,11,1,11,3,11,155,8,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,3,14,176,8,14,1,15,1,15,1,15,1,16,1,16,1,16,3,16,184,8,16,1,
        17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,3,19,194,8,19,1,20,1,20,1,
        21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,3,23,206,8,23,1,24,1,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,217,8,25,1,26,3,26,220,8,26,
        1,27,1,27,3,27,224,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,3,29,238,8,29,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,3,31,247,8,31,1,32,3,32,250,8,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,34,3,34,259,8,34,1,35,1,35,1,35,1,36,1,36,3,36,266,8,36,1,36,
        0,1,6,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,5,1,0,8,9,1,
        0,20,22,1,0,23,24,1,0,31,32,1,0,25,26,254,0,74,1,0,0,0,2,90,1,0,
        0,0,4,96,1,0,0,0,6,102,1,0,0,0,8,114,1,0,0,0,10,116,1,0,0,0,12,118,
        1,0,0,0,14,132,1,0,0,0,16,134,1,0,0,0,18,139,1,0,0,0,20,150,1,0,
        0,0,22,154,1,0,0,0,24,156,1,0,0,0,26,164,1,0,0,0,28,175,1,0,0,0,
        30,177,1,0,0,0,32,183,1,0,0,0,34,185,1,0,0,0,36,187,1,0,0,0,38,193,
        1,0,0,0,40,195,1,0,0,0,42,197,1,0,0,0,44,199,1,0,0,0,46,205,1,0,
        0,0,48,207,1,0,0,0,50,216,1,0,0,0,52,219,1,0,0,0,54,223,1,0,0,0,
        56,225,1,0,0,0,58,237,1,0,0,0,60,239,1,0,0,0,62,246,1,0,0,0,64,249,
        1,0,0,0,66,251,1,0,0,0,68,258,1,0,0,0,70,260,1,0,0,0,72,265,1,0,
        0,0,74,75,5,1,0,0,75,76,5,30,0,0,76,78,5,2,0,0,77,79,3,2,1,0,78,
        77,1,0,0,0,78,79,1,0,0,0,79,83,1,0,0,0,80,82,3,56,28,0,81,80,1,0,
        0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,
        1,0,0,0,86,87,5,3,0,0,87,88,3,12,6,0,88,89,5,4,0,0,89,1,1,0,0,0,
        90,92,5,5,0,0,91,93,3,4,2,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,3,1,0,0,0,96,97,3,6,3,0,97,98,5,6,0,0,98,
        99,3,10,5,0,99,100,5,2,0,0,100,101,3,8,4,0,101,5,1,0,0,0,102,103,
        6,3,-1,0,103,104,5,30,0,0,104,110,1,0,0,0,105,106,10,1,0,0,106,107,
        5,7,0,0,107,109,5,30,0,0,108,105,1,0,0,0,109,112,1,0,0,0,110,108,
        1,0,0,0,110,111,1,0,0,0,111,7,1,0,0,0,112,110,1,0,0,0,113,115,3,
        6,3,0,114,113,1,0,0,0,114,115,1,0,0,0,115,9,1,0,0,0,116,117,7,0,
        0,0,117,11,1,0,0,0,118,122,5,10,0,0,119,121,3,14,7,0,120,119,1,0,
        0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,
        0,0,124,122,1,0,0,0,125,126,5,11,0,0,126,13,1,0,0,0,127,133,3,16,
        8,0,128,133,3,26,13,0,129,133,3,24,12,0,130,133,3,66,33,0,131,133,
        3,18,9,0,132,127,1,0,0,0,132,128,1,0,0,0,132,129,1,0,0,0,132,130,
        1,0,0,0,132,131,1,0,0,0,133,15,1,0,0,0,134,135,5,30,0,0,135,136,
        5,12,0,0,136,137,3,30,15,0,137,138,5,2,0,0,138,17,1,0,0,0,139,140,
        5,13,0,0,140,141,5,14,0,0,141,142,3,20,10,0,142,143,5,15,0,0,143,
        144,5,2,0,0,144,19,1,0,0,0,145,146,3,30,15,0,146,147,3,22,11,0,147,
        151,1,0,0,0,148,149,5,33,0,0,149,151,3,22,11,0,150,145,1,0,0,0,150,
        148,1,0,0,0,151,21,1,0,0,0,152,153,5,7,0,0,153,155,3,20,10,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,23,1,0,0,0,156,157,5,16,0,0,157,
        158,3,12,6,0,158,159,5,17,0,0,159,160,5,14,0,0,160,161,3,30,15,0,
        161,162,5,15,0,0,162,163,5,2,0,0,163,25,1,0,0,0,164,165,5,18,0,0,
        165,166,5,14,0,0,166,167,3,30,15,0,167,168,5,15,0,0,168,169,3,12,
        6,0,169,170,3,28,14,0,170,27,1,0,0,0,171,172,5,19,0,0,172,173,3,
        12,6,0,173,174,5,2,0,0,174,176,1,0,0,0,175,171,1,0,0,0,175,176,1,
        0,0,0,176,29,1,0,0,0,177,178,3,36,18,0,178,179,3,32,16,0,179,31,
        1,0,0,0,180,181,3,34,17,0,181,182,3,36,18,0,182,184,1,0,0,0,183,
        180,1,0,0,0,183,184,1,0,0,0,184,33,1,0,0,0,185,186,7,1,0,0,186,35,
        1,0,0,0,187,188,3,44,22,0,188,189,3,38,19,0,189,37,1,0,0,0,190,191,
        3,40,20,0,191,192,3,36,18,0,192,194,1,0,0,0,193,190,1,0,0,0,193,
        194,1,0,0,0,194,39,1,0,0,0,195,196,7,2,0,0,196,41,1,0,0,0,197,198,
        7,3,0,0,198,43,1,0,0,0,199,200,3,50,25,0,200,201,3,46,23,0,201,45,
        1,0,0,0,202,203,3,48,24,0,203,204,3,44,22,0,204,206,1,0,0,0,205,
        202,1,0,0,0,205,206,1,0,0,0,206,47,1,0,0,0,207,208,7,4,0,0,208,49,
        1,0,0,0,209,210,5,14,0,0,210,211,3,30,15,0,211,212,5,15,0,0,212,
        217,1,0,0,0,213,214,3,52,26,0,214,215,3,54,27,0,215,217,1,0,0,0,
        216,209,1,0,0,0,216,213,1,0,0,0,217,51,1,0,0,0,218,220,7,2,0,0,219,
        218,1,0,0,0,219,220,1,0,0,0,220,53,1,0,0,0,221,224,5,30,0,0,222,
        224,3,42,21,0,223,221,1,0,0,0,223,222,1,0,0,0,224,55,1,0,0,0,225,
        226,5,27,0,0,226,227,5,30,0,0,227,228,5,14,0,0,228,229,3,58,29,0,
        229,230,5,15,0,0,230,231,5,28,0,0,231,232,3,64,32,0,232,233,3,12,
        6,0,233,234,5,29,0,0,234,235,5,2,0,0,235,57,1,0,0,0,236,238,3,60,
        30,0,237,236,1,0,0,0,237,238,1,0,0,0,238,59,1,0,0,0,239,240,5,30,
        0,0,240,241,5,6,0,0,241,242,3,10,5,0,242,243,3,62,31,0,243,61,1,
        0,0,0,244,245,5,7,0,0,245,247,3,60,30,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,63,1,0,0,0,248,250,3,2,1,0,249,248,1,0,0,0,249,250,1,
        0,0,0,250,65,1,0,0,0,251,252,5,30,0,0,252,253,5,14,0,0,253,254,3,
        68,34,0,254,255,5,15,0,0,255,256,5,2,0,0,256,67,1,0,0,0,257,259,
        3,70,35,0,258,257,1,0,0,0,258,259,1,0,0,0,259,69,1,0,0,0,260,261,
        3,30,15,0,261,262,3,72,36,0,262,71,1,0,0,0,263,264,5,7,0,0,264,266,
        3,70,35,0,265,263,1,0,0,0,265,266,1,0,0,0,266,73,1,0,0,0,21,78,83,
        94,110,114,122,132,150,154,175,183,193,205,216,219,223,237,246,249,
        258,265
    ]

class little_duckParser ( Parser ):

    grammarFileName = "little_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'float'", "'int'", "'{'", "'}'", 
                     "'='", "'printf'", "'('", "')'", "'do'", "'while'", 
                     "'if'", "'else'", "'>'", "'<'", "'!='", "'-'", "'+'", 
                     "'*'", "'/'", "'void'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "CTE_FLOAT", "CTE_INT", 
                      "CTE_STRING", "WS" ]

    RULE_start_ = 0
    RULE_vars = 1
    RULE_var0 = 2
    RULE_var1 = 3
    RULE_var2 = 4
    RULE_type = 5
    RULE_body = 6
    RULE_statement = 7
    RULE_assign = 8
    RULE_print = 9
    RULE_print0 = 10
    RULE_print1 = 11
    RULE_cycle = 12
    RULE_condition = 13
    RULE_condition0 = 14
    RULE_expression = 15
    RULE_expression0 = 16
    RULE_expression1 = 17
    RULE_exp = 18
    RULE_exp0 = 19
    RULE_exp1 = 20
    RULE_cte = 21
    RULE_termino = 22
    RULE_termino0 = 23
    RULE_termino1 = 24
    RULE_factor = 25
    RULE_factor0 = 26
    RULE_factor1 = 27
    RULE_funcs = 28
    RULE_funcs0 = 29
    RULE_funcs1 = 30
    RULE_funcs2 = 31
    RULE_funcs3 = 32
    RULE_f_call = 33
    RULE_f_call0 = 34
    RULE_f_call1 = 35
    RULE_f_call2 = 36

    ruleNames =  [ "start_", "vars", "var0", "var1", "var2", "type", "body", 
                   "statement", "assign", "print", "print0", "print1", "cycle", 
                   "condition", "condition0", "expression", "expression0", 
                   "expression1", "exp", "exp0", "exp1", "cte", "termino", 
                   "termino0", "termino1", "factor", "factor0", "factor1", 
                   "funcs", "funcs0", "funcs1", "funcs2", "funcs3", "f_call", 
                   "f_call0", "f_call1", "f_call2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    ID=30
    CTE_FLOAT=31
    CTE_INT=32
    CTE_STRING=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def vars_(self):
            return self.getTypedRuleContext(little_duckParser.VarsContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(little_duckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(little_duckParser.FuncsContext,i)


        def getRuleIndex(self):
            return little_duckParser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)




    def start_(self):

        localctx = little_duckParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(little_duckParser.T__0)
            self.state = 75
            self.match(little_duckParser.ID)
            self.state = 76
            self.match(little_duckParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 77
                self.vars_()


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 80
                self.funcs()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(little_duckParser.T__2)
            self.state = 87
            self.body()
            self.state = 88
            self.match(little_duckParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(little_duckParser.Var0Context)
            else:
                return self.getTypedRuleContext(little_duckParser.Var0Context,i)


        def getRuleIndex(self):
            return little_duckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = little_duckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(little_duckParser.T__4)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.var0()
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==30):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var1(self):
            return self.getTypedRuleContext(little_duckParser.Var1Context,0)


        def type_(self):
            return self.getTypedRuleContext(little_duckParser.TypeContext,0)


        def var2(self):
            return self.getTypedRuleContext(little_duckParser.Var2Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_var0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar0" ):
                listener.enterVar0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar0" ):
                listener.exitVar0(self)




    def var0(self):

        localctx = little_duckParser.Var0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.var1(0)
            self.state = 97
            self.match(little_duckParser.T__5)
            self.state = 98
            self.type_()
            self.state = 99
            self.match(little_duckParser.T__1)
            self.state = 100
            self.var2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def var1(self):
            return self.getTypedRuleContext(little_duckParser.Var1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_var1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar1" ):
                listener.enterVar1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar1" ):
                listener.exitVar1(self)



    def var1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = little_duckParser.Var1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_var1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(little_duckParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = little_duckParser.Var1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var1)
                    self.state = 105
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 106
                    self.match(little_duckParser.T__6)
                    self.state = 107
                    self.match(little_duckParser.ID) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Var2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var1(self):
            return self.getTypedRuleContext(little_duckParser.Var1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_var2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar2" ):
                listener.enterVar2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar2" ):
                listener.exitVar2(self)




    def var2(self):

        localctx = little_duckParser.Var2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 113
                self.var1(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = little_duckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(little_duckParser.StatementContext)
            else:
                return self.getTypedRuleContext(little_duckParser.StatementContext,i)


        def getRuleIndex(self):
            return little_duckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = little_duckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(little_duckParser.T__9)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1074077696) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(little_duckParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(little_duckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(little_duckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(little_duckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(little_duckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(little_duckParser.PrintContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = little_duckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = little_duckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(little_duckParser.ID)
            self.state = 135
            self.match(little_duckParser.T__11)
            self.state = 136
            self.expression()
            self.state = 137
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print0(self):
            return self.getTypedRuleContext(little_duckParser.Print0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = little_duckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(little_duckParser.T__12)
            self.state = 140
            self.match(little_duckParser.T__13)
            self.state = 141
            self.print0()
            self.state = 142
            self.match(little_duckParser.T__14)
            self.state = 143
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def print1(self):
            return self.getTypedRuleContext(little_duckParser.Print1Context,0)


        def CTE_STRING(self):
            return self.getToken(little_duckParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return little_duckParser.RULE_print0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint0" ):
                listener.enterPrint0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint0" ):
                listener.exitPrint0(self)




    def print0(self):

        localctx = little_duckParser.Print0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print0)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 23, 24, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.expression()
                self.state = 146
                self.print1()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(little_duckParser.CTE_STRING)
                self.state = 149
                self.print1()
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


    class Print1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print0(self):
            return self.getTypedRuleContext(little_duckParser.Print0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_print1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint1" ):
                listener.enterPrint1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint1" ):
                listener.exitPrint1(self)




    def print1(self):

        localctx = little_duckParser.Print1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 152
                self.match(little_duckParser.T__6)
                self.state = 153
                self.print0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = little_duckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(little_duckParser.T__15)
            self.state = 157
            self.body()
            self.state = 158
            self.match(little_duckParser.T__16)
            self.state = 159
            self.match(little_duckParser.T__13)
            self.state = 160
            self.expression()
            self.state = 161
            self.match(little_duckParser.T__14)
            self.state = 162
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def condition0(self):
            return self.getTypedRuleContext(little_duckParser.Condition0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = little_duckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(little_duckParser.T__17)
            self.state = 165
            self.match(little_duckParser.T__13)
            self.state = 166
            self.expression()
            self.state = 167
            self.match(little_duckParser.T__14)
            self.state = 168
            self.body()
            self.state = 169
            self.condition0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_condition0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition0" ):
                listener.enterCondition0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition0" ):
                listener.exitCondition0(self)




    def condition0(self):

        localctx = little_duckParser.Condition0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 171
                self.match(little_duckParser.T__18)
                self.state = 172
                self.body()
                self.state = 173
                self.match(little_duckParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(little_duckParser.ExpContext,0)


        def expression0(self):
            return self.getTypedRuleContext(little_duckParser.Expression0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = little_duckParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.exp()
            self.state = 178
            self.expression0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(little_duckParser.Expression1Context,0)


        def exp(self):
            return self.getTypedRuleContext(little_duckParser.ExpContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_expression0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression0" ):
                listener.enterExpression0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression0" ):
                listener.exitExpression0(self)




    def expression0(self):

        localctx = little_duckParser.Expression0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                self.state = 180
                self.expression1()
                self.state = 181
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_expression1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression1" ):
                listener.enterExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression1" ):
                listener.exitExpression1(self)




    def expression1(self):

        localctx = little_duckParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(little_duckParser.TerminoContext,0)


        def exp0(self):
            return self.getTypedRuleContext(little_duckParser.Exp0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = little_duckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.termino()
            self.state = 188
            self.exp0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(little_duckParser.Exp1Context,0)


        def exp(self):
            return self.getTypedRuleContext(little_duckParser.ExpContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_exp0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp0" ):
                listener.enterExp0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp0" ):
                listener.exitExp0(self)




    def exp0(self):

        localctx = little_duckParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23 or _la==24:
                self.state = 190
                self.exp1()
                self.state = 191
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_exp1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp1" ):
                listener.enterExp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp1" ):
                listener.exitExp1(self)




    def exp1(self):

        localctx = little_duckParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_FLOAT(self):
            return self.getToken(little_duckParser.CTE_FLOAT, 0)

        def CTE_INT(self):
            return self.getToken(little_duckParser.CTE_INT, 0)

        def getRuleIndex(self):
            return little_duckParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = little_duckParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(little_duckParser.FactorContext,0)


        def termino0(self):
            return self.getTypedRuleContext(little_duckParser.Termino0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = little_duckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.factor()
            self.state = 200
            self.termino0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termino0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino1(self):
            return self.getTypedRuleContext(little_duckParser.Termino1Context,0)


        def termino(self):
            return self.getTypedRuleContext(little_duckParser.TerminoContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_termino0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino0" ):
                listener.enterTermino0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino0" ):
                listener.exitTermino0(self)




    def termino0(self):

        localctx = little_duckParser.Termino0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_termino0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 202
                self.termino1()
                self.state = 203
                self.termino()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termino1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_termino1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino1" ):
                listener.enterTermino1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino1" ):
                listener.exitTermino1(self)




    def termino1(self):

        localctx = little_duckParser.Termino1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_termino1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def factor0(self):
            return self.getTypedRuleContext(little_duckParser.Factor0Context,0)


        def factor1(self):
            return self.getTypedRuleContext(little_duckParser.Factor1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = little_duckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(little_duckParser.T__13)
                self.state = 210
                self.expression()
                self.state = 211
                self.match(little_duckParser.T__14)
                pass
            elif token in [23, 24, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.factor0()
                self.state = 214
                self.factor1()
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


    class Factor0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_factor0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor0" ):
                listener.enterFactor0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor0" ):
                listener.exitFactor0(self)




    def factor0(self):

        localctx = little_duckParser.Factor0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23 or _la==24:
                self.state = 218
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
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


    class Factor1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(little_duckParser.CteContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_factor1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor1" ):
                listener.enterFactor1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor1" ):
                listener.exitFactor1(self)




    def factor1(self):

        localctx = little_duckParser.Factor1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_factor1)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(little_duckParser.ID)
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.cte()
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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def funcs0(self):
            return self.getTypedRuleContext(little_duckParser.Funcs0Context,0)


        def funcs3(self):
            return self.getTypedRuleContext(little_duckParser.Funcs3Context,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = little_duckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(little_duckParser.T__26)
            self.state = 226
            self.match(little_duckParser.ID)
            self.state = 227
            self.match(little_duckParser.T__13)
            self.state = 228
            self.funcs0()
            self.state = 229
            self.match(little_duckParser.T__14)
            self.state = 230
            self.match(little_duckParser.T__27)
            self.state = 231
            self.funcs3()
            self.state = 232
            self.body()
            self.state = 233
            self.match(little_duckParser.T__28)
            self.state = 234
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs1(self):
            return self.getTypedRuleContext(little_duckParser.Funcs1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs0" ):
                listener.enterFuncs0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs0" ):
                listener.exitFuncs0(self)




    def funcs0(self):

        localctx = little_duckParser.Funcs0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcs0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 236
                self.funcs1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(little_duckParser.TypeContext,0)


        def funcs2(self):
            return self.getTypedRuleContext(little_duckParser.Funcs2Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs1" ):
                listener.enterFuncs1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs1" ):
                listener.exitFuncs1(self)




    def funcs1(self):

        localctx = little_duckParser.Funcs1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_funcs1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(little_duckParser.ID)
            self.state = 240
            self.match(little_duckParser.T__5)
            self.state = 241
            self.type_()
            self.state = 242
            self.funcs2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs1(self):
            return self.getTypedRuleContext(little_duckParser.Funcs1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs2" ):
                listener.enterFuncs2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs2" ):
                listener.exitFuncs2(self)




    def funcs2(self):

        localctx = little_duckParser.Funcs2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcs2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 244
                self.match(little_duckParser.T__6)
                self.state = 245
                self.funcs1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(little_duckParser.VarsContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs3" ):
                listener.enterFuncs3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs3" ):
                listener.exitFuncs3(self)




    def funcs3(self):

        localctx = little_duckParser.Funcs3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funcs3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 248
                self.vars_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def f_call0(self):
            return self.getTypedRuleContext(little_duckParser.F_call0Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = little_duckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(little_duckParser.ID)
            self.state = 252
            self.match(little_duckParser.T__13)
            self.state = 253
            self.f_call0()
            self.state = 254
            self.match(little_duckParser.T__14)
            self.state = 255
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_call1(self):
            return self.getTypedRuleContext(little_duckParser.F_call1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call0" ):
                listener.enterF_call0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call0" ):
                listener.exitF_call0(self)




    def f_call0(self):

        localctx = little_duckParser.F_call0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_f_call0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7541374976) != 0):
                self.state = 257
                self.f_call1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def f_call2(self):
            return self.getTypedRuleContext(little_duckParser.F_call2Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call1" ):
                listener.enterF_call1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call1" ):
                listener.exitF_call1(self)




    def f_call1(self):

        localctx = little_duckParser.F_call1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_f_call1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expression()
            self.state = 261
            self.f_call2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_call1(self):
            return self.getTypedRuleContext(little_duckParser.F_call1Context,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call2" ):
                listener.enterF_call2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call2" ):
                listener.exitF_call2(self)




    def f_call2(self):

        localctx = little_duckParser.F_call2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_f_call2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 263
                self.match(little_duckParser.T__6)
                self.state = 264
                self.f_call1()


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
        self._predicates[3] = self.var1_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def var1_sempred(self, localctx:Var1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




