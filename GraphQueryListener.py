# Generated from project/GraphQuery.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GraphQueryParser import GraphQueryParser
else:
    from GraphQueryParser import GraphQueryParser

# This class defines a complete listener for a parse tree produced by GraphQueryParser.
class GraphQueryListener(ParseTreeListener):

    # Enter a parse tree produced by GraphQueryParser#prog.
    def enterProg(self, ctx:GraphQueryParser.ProgContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#prog.
    def exitProg(self, ctx:GraphQueryParser.ProgContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#stmt.
    def enterStmt(self, ctx:GraphQueryParser.StmtContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#stmt.
    def exitStmt(self, ctx:GraphQueryParser.StmtContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#declare.
    def enterDeclare(self, ctx:GraphQueryParser.DeclareContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#declare.
    def exitDeclare(self, ctx:GraphQueryParser.DeclareContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#bind.
    def enterBind(self, ctx:GraphQueryParser.BindContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#bind.
    def exitBind(self, ctx:GraphQueryParser.BindContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#remove.
    def enterRemove(self, ctx:GraphQueryParser.RemoveContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#remove.
    def exitRemove(self, ctx:GraphQueryParser.RemoveContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#add.
    def enterAdd(self, ctx:GraphQueryParser.AddContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#add.
    def exitAdd(self, ctx:GraphQueryParser.AddContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#expr.
    def enterExpr(self, ctx:GraphQueryParser.ExprContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#expr.
    def exitExpr(self, ctx:GraphQueryParser.ExprContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#set_expr.
    def enterSet_expr(self, ctx:GraphQueryParser.Set_exprContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#set_expr.
    def exitSet_expr(self, ctx:GraphQueryParser.Set_exprContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#edge_expr.
    def enterEdge_expr(self, ctx:GraphQueryParser.Edge_exprContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#edge_expr.
    def exitEdge_expr(self, ctx:GraphQueryParser.Edge_exprContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#regexp.
    def enterRegexp(self, ctx:GraphQueryParser.RegexpContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#regexp.
    def exitRegexp(self, ctx:GraphQueryParser.RegexpContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#primary_regexp.
    def enterPrimary_regexp(self, ctx:GraphQueryParser.Primary_regexpContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#primary_regexp.
    def exitPrimary_regexp(self, ctx:GraphQueryParser.Primary_regexpContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#range.
    def enterRange(self, ctx:GraphQueryParser.RangeContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#range.
    def exitRange(self, ctx:GraphQueryParser.RangeContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#select.
    def enterSelect(self, ctx:GraphQueryParser.SelectContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#select.
    def exitSelect(self, ctx:GraphQueryParser.SelectContext):
        pass


    # Enter a parse tree produced by GraphQueryParser#v_filter.
    def enterV_filter(self, ctx:GraphQueryParser.V_filterContext):
        pass

    # Exit a parse tree produced by GraphQueryParser#v_filter.
    def exitV_filter(self, ctx:GraphQueryParser.V_filterContext):
        pass



del GraphQueryParser