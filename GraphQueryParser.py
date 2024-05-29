# Generated from project/GraphQuery.g4 by ANTLR 4.13.1
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
        4,1,31,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,70,8,6,1,7,1,7,
        1,7,1,7,5,7,76,8,7,10,7,12,7,79,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,5,9,94,8,9,10,9,12,9,97,9,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,114,8,10,1,11,1,11,1,11,1,11,3,11,120,8,11,1,11,1,11,1,12,3,12,
        125,8,12,1,12,3,12,128,8,12,1,12,1,12,1,12,1,12,3,12,134,8,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,1,0,
        6,8,1,0,6,7,157,0,31,1,0,0,0,2,38,1,0,0,0,4,40,1,0,0,0,6,45,1,0,
        0,0,8,50,1,0,0,0,10,56,1,0,0,0,12,69,1,0,0,0,14,71,1,0,0,0,16,82,
        1,0,0,0,18,90,1,0,0,0,20,113,1,0,0,0,22,115,1,0,0,0,24,124,1,0,0,
        0,26,145,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,
        1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,31,1,0,0,0,34,39,3,6,3,0,35,
        39,3,10,5,0,36,39,3,8,4,0,37,39,3,4,2,0,38,34,1,0,0,0,38,35,1,0,
        0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,1,0,0,41,42,
        5,27,0,0,42,43,5,2,0,0,43,44,5,3,0,0,44,5,1,0,0,0,45,46,5,1,0,0,
        46,47,5,27,0,0,47,48,5,4,0,0,48,49,3,12,6,0,49,7,1,0,0,0,50,51,5,
        5,0,0,51,52,7,0,0,0,52,53,3,12,6,0,53,54,5,9,0,0,54,55,5,27,0,0,
        55,9,1,0,0,0,56,57,5,10,0,0,57,58,7,1,0,0,58,59,3,12,6,0,59,60,5,
        11,0,0,60,61,5,27,0,0,61,11,1,0,0,0,62,70,5,28,0,0,63,70,5,29,0,
        0,64,70,5,27,0,0,65,70,3,16,8,0,66,70,3,14,7,0,67,70,3,18,9,0,68,
        70,3,24,12,0,69,62,1,0,0,0,69,63,1,0,0,0,69,64,1,0,0,0,69,65,1,0,
        0,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,13,1,0,0,0,71,72,
        5,12,0,0,72,77,3,12,6,0,73,74,5,13,0,0,74,76,3,12,6,0,75,73,1,0,
        0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,
        1,0,0,0,80,81,5,14,0,0,81,15,1,0,0,0,82,83,5,15,0,0,83,84,3,12,6,
        0,84,85,5,13,0,0,85,86,3,12,6,0,86,87,5,13,0,0,87,88,3,12,6,0,88,
        89,5,16,0,0,89,17,1,0,0,0,90,95,3,20,10,0,91,92,5,30,0,0,92,94,3,
        20,10,0,93,91,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,
        96,19,1,0,0,0,97,95,1,0,0,0,98,114,5,29,0,0,99,114,5,27,0,0,100,
        101,5,15,0,0,101,102,3,18,9,0,102,103,5,16,0,0,103,114,1,0,0,0,104,
        105,5,29,0,0,105,106,5,17,0,0,106,114,3,22,11,0,107,108,5,29,0,0,
        108,109,5,18,0,0,109,114,5,29,0,0,110,111,5,29,0,0,111,112,5,19,
        0,0,112,114,5,29,0,0,113,98,1,0,0,0,113,99,1,0,0,0,113,100,1,0,0,
        0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,1,0,0,0,114,21,1,0,0,0,
        115,116,5,12,0,0,116,117,5,28,0,0,117,119,5,20,0,0,118,120,5,28,
        0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,5,14,
        0,0,122,23,1,0,0,0,123,125,3,26,13,0,124,123,1,0,0,0,124,125,1,0,
        0,0,125,127,1,0,0,0,126,128,3,26,13,0,127,126,1,0,0,0,127,128,1,
        0,0,0,128,129,1,0,0,0,129,130,5,21,0,0,130,133,5,27,0,0,131,132,
        5,13,0,0,132,134,5,27,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,135,
        1,0,0,0,135,136,5,22,0,0,136,137,5,27,0,0,137,138,5,23,0,0,138,139,
        5,9,0,0,139,140,5,27,0,0,140,141,5,24,0,0,141,142,5,27,0,0,142,143,
        5,25,0,0,143,144,3,12,6,0,144,25,1,0,0,0,145,146,5,26,0,0,146,147,
        5,27,0,0,147,148,5,24,0,0,148,149,3,12,6,0,149,27,1,0,0,0,10,31,
        38,69,77,95,113,119,124,127,133
    ]

class GraphQueryParser ( Parser ):

    grammarFileName = "GraphQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'is'", "'graph'", "'='", "'remove'", 
                     "'vertex'", "'edge'", "'vertices'", "'from'", "'add'", 
                     "'to'", "'['", "','", "']'", "'('", "')'", "'^'", "'.'", 
                     "'&'", "'..'", "'return'", "'where'", "'reachable'", 
                     "'in'", "'by'", "'for'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VAR", "NUM", 
                      "CHAR", "REGEXP_OP", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_declare = 2
    RULE_bind = 3
    RULE_remove = 4
    RULE_add = 5
    RULE_expr = 6
    RULE_set_expr = 7
    RULE_edge_expr = 8
    RULE_regexp = 9
    RULE_primary_regexp = 10
    RULE_range = 11
    RULE_select = 12
    RULE_v_filter = 13

    ruleNames =  [ "prog", "stmt", "declare", "bind", "remove", "add", "expr", 
                   "set_expr", "edge_expr", "regexp", "primary_regexp", 
                   "range", "select", "v_filter" ]

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
    VAR=27
    NUM=28
    CHAR=29
    REGEXP_OP=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryParser.StmtContext)
            else:
                return self.getTypedRuleContext(GraphQueryParser.StmtContext,i)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = GraphQueryParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1058) != 0):
                self.state = 28
                self.stmt()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def bind(self):
            return self.getTypedRuleContext(GraphQueryParser.BindContext,0)


        def add(self):
            return self.getTypedRuleContext(GraphQueryParser.AddContext,0)


        def remove(self):
            return self.getTypedRuleContext(GraphQueryParser.RemoveContext,0)


        def declare(self):
            return self.getTypedRuleContext(GraphQueryParser.DeclareContext,0)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = GraphQueryParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.bind()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.add()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.remove()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def getRuleIndex(self):
            return GraphQueryParser.RULE_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare" ):
                listener.enterDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare" ):
                listener.exitDeclare(self)




    def declare(self):

        localctx = GraphQueryParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(GraphQueryParser.T__0)
            self.state = 41
            self.match(GraphQueryParser.VAR)
            self.state = 42
            self.match(GraphQueryParser.T__1)
            self.state = 43
            self.match(GraphQueryParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryParser.ExprContext,0)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_bind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBind" ):
                listener.enterBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBind" ):
                listener.exitBind(self)




    def bind(self):

        localctx = GraphQueryParser.BindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GraphQueryParser.T__0)
            self.state = 46
            self.match(GraphQueryParser.VAR)
            self.state = 47
            self.match(GraphQueryParser.T__3)
            self.state = 48
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GraphQueryParser.ExprContext,0)


        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def getRuleIndex(self):
            return GraphQueryParser.RULE_remove

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove" ):
                listener.enterRemove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove" ):
                listener.exitRemove(self)




    def remove(self):

        localctx = GraphQueryParser.RemoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_remove)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(GraphQueryParser.T__4)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 52
            self.expr()
            self.state = 53
            self.match(GraphQueryParser.T__8)
            self.state = 54
            self.match(GraphQueryParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GraphQueryParser.ExprContext,0)


        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def getRuleIndex(self):
            return GraphQueryParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)




    def add(self):

        localctx = GraphQueryParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(GraphQueryParser.T__9)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.expr()
            self.state = 59
            self.match(GraphQueryParser.T__10)
            self.state = 60
            self.match(GraphQueryParser.VAR)
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

        def NUM(self):
            return self.getToken(GraphQueryParser.NUM, 0)

        def CHAR(self):
            return self.getToken(GraphQueryParser.CHAR, 0)

        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def edge_expr(self):
            return self.getTypedRuleContext(GraphQueryParser.Edge_exprContext,0)


        def set_expr(self):
            return self.getTypedRuleContext(GraphQueryParser.Set_exprContext,0)


        def regexp(self):
            return self.getTypedRuleContext(GraphQueryParser.RegexpContext,0)


        def select(self):
            return self.getTypedRuleContext(GraphQueryParser.SelectContext,0)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = GraphQueryParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(GraphQueryParser.NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(GraphQueryParser.CHAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(GraphQueryParser.VAR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.edge_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.set_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.regexp()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.select()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphQueryParser.ExprContext,i)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_set_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_expr" ):
                listener.enterSet_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_expr" ):
                listener.exitSet_expr(self)




    def set_expr(self):

        localctx = GraphQueryParser.Set_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_set_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GraphQueryParser.T__11)
            self.state = 72
            self.expr()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 73
                self.match(GraphQueryParser.T__12)
                self.state = 74
                self.expr()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(GraphQueryParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphQueryParser.ExprContext,i)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_edge_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_expr" ):
                listener.enterEdge_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_expr" ):
                listener.exitEdge_expr(self)




    def edge_expr(self):

        localctx = GraphQueryParser.Edge_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_edge_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GraphQueryParser.T__14)
            self.state = 83
            self.expr()
            self.state = 84
            self.match(GraphQueryParser.T__12)
            self.state = 85
            self.expr()
            self.state = 86
            self.match(GraphQueryParser.T__12)
            self.state = 87
            self.expr()
            self.state = 88
            self.match(GraphQueryParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def primary_regexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryParser.Primary_regexpContext)
            else:
                return self.getTypedRuleContext(GraphQueryParser.Primary_regexpContext,i)


        def REGEXP_OP(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueryParser.REGEXP_OP)
            else:
                return self.getToken(GraphQueryParser.REGEXP_OP, i)

        def getRuleIndex(self):
            return GraphQueryParser.RULE_regexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegexp" ):
                listener.enterRegexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegexp" ):
                listener.exitRegexp(self)




    def regexp(self):

        localctx = GraphQueryParser.RegexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_regexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.primary_regexp()

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 91
                localctx.op = self.match(GraphQueryParser.REGEXP_OP)
                self.state = 92
                self.primary_regexp()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_regexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueryParser.CHAR)
            else:
                return self.getToken(GraphQueryParser.CHAR, i)

        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def regexp(self):
            return self.getTypedRuleContext(GraphQueryParser.RegexpContext,0)


        def range_(self):
            return self.getTypedRuleContext(GraphQueryParser.RangeContext,0)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_primary_regexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_regexp" ):
                listener.enterPrimary_regexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_regexp" ):
                listener.exitPrimary_regexp(self)




    def primary_regexp(self):

        localctx = GraphQueryParser.Primary_regexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary_regexp)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(GraphQueryParser.CHAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(GraphQueryParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(GraphQueryParser.T__14)
                self.state = 101
                self.regexp()
                self.state = 102
                self.match(GraphQueryParser.T__15)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(GraphQueryParser.CHAR)
                self.state = 105
                self.match(GraphQueryParser.T__16)
                self.state = 106
                self.range_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.match(GraphQueryParser.CHAR)
                self.state = 108
                self.match(GraphQueryParser.T__17)
                self.state = 109
                self.match(GraphQueryParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.match(GraphQueryParser.CHAR)
                self.state = 111
                self.match(GraphQueryParser.T__18)
                self.state = 112
                self.match(GraphQueryParser.CHAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueryParser.NUM)
            else:
                return self.getToken(GraphQueryParser.NUM, i)

        def getRuleIndex(self):
            return GraphQueryParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)




    def range_(self):

        localctx = GraphQueryParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(GraphQueryParser.T__11)
            self.state = 116
            self.match(GraphQueryParser.NUM)
            self.state = 117
            self.match(GraphQueryParser.T__19)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 118
                self.match(GraphQueryParser.NUM)


            self.state = 121
            self.match(GraphQueryParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueryParser.VAR)
            else:
                return self.getToken(GraphQueryParser.VAR, i)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryParser.ExprContext,0)


        def v_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryParser.V_filterContext)
            else:
                return self.getTypedRuleContext(GraphQueryParser.V_filterContext,i)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = GraphQueryParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 123
                self.v_filter()


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 126
                self.v_filter()


            self.state = 129
            self.match(GraphQueryParser.T__20)
            self.state = 130
            self.match(GraphQueryParser.VAR)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 131
                self.match(GraphQueryParser.T__12)
                self.state = 132
                self.match(GraphQueryParser.VAR)


            self.state = 135
            self.match(GraphQueryParser.T__21)
            self.state = 136
            self.match(GraphQueryParser.VAR)
            self.state = 137
            self.match(GraphQueryParser.T__22)
            self.state = 138
            self.match(GraphQueryParser.T__8)
            self.state = 139
            self.match(GraphQueryParser.VAR)
            self.state = 140
            self.match(GraphQueryParser.T__23)
            self.state = 141
            self.match(GraphQueryParser.VAR)
            self.state = 142
            self.match(GraphQueryParser.T__24)
            self.state = 143
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_filterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GraphQueryParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryParser.ExprContext,0)


        def getRuleIndex(self):
            return GraphQueryParser.RULE_v_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_filter" ):
                listener.enterV_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_filter" ):
                listener.exitV_filter(self)




    def v_filter(self):

        localctx = GraphQueryParser.V_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_v_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(GraphQueryParser.T__25)
            self.state = 146
            self.match(GraphQueryParser.VAR)
            self.state = 147
            self.match(GraphQueryParser.T__23)
            self.state = 148
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





