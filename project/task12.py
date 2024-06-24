import networkx as nx
from antlr4 import CommonTokenStream, InputStream
from pyformlang.finite_automaton import *
from pyformlang.regular_expression import *
import project.task3 as fau
from collections import defaultdict

import networkx as nx
from pyformlang.finite_automaton import *
from pyformlang.regular_expression import *
from scipy.sparse import *
import project.task1 as gu
from project.GraphQueryParser import GraphQueryParser
from project.GraphQueryVisitor import GraphQueryVisitor
from project.GraphQueryLexer import GraphQueryLexer


def build_NDFA_from_graph(
        graph: nx.DiGraph, start: set[State] = None, final: set[State] = None
) -> EpsilonNFA:
    """
    Builds NDFA from graph representation, start and final nodes
    :param graph: Graph representation of the resulting NDFA
    :param start: Start states of the resulting NDFA. If None - all states are considered start states
    :param final: Final states of the resulting NDFA. If None - all states are considered final states
    :return: NDFA built from graph representation, start and final nodes
    """
    ndfa = EpsilonNFA.from_networkx(graph)

    for s, f, label in graph.edges(data="label"):
        ndfa.add_transition(s, label, f)

    if start is not None:
        for s in start:
            ndfa.add_start_state(s)
    else:
        for s in ndfa.states:
            ndfa.add_start_state(s)
    if final is not None:
        for s in final:
            ndfa.add_final_state(s)
    else:
        for s in ndfa.states:
            ndfa.add_final_state(s)

    return ndfa
class Visitor(GraphQueryVisitor):
    class ID:
        def __init__(self, val: str):
            self.value = val

    def __init__(self):
        self.vars = dict()

    def extractExprResult(self, expr_ctx):
        if expr_ctx is None:
            return None
        expr_r = expr_ctx.accept(self)
        if isinstance(expr_r, Visitor.ID) and expr_r.value in self.vars:
            return self.vars[expr_r.value]
        else:
            return expr_r

    @staticmethod
    def isIterable(obj):
        try:
            t = iter(obj)
            return True
        except TypeError:
            return False

    def visitOp(self, ctx: GraphQueryParser.OpContext):
        expr_c = ctx.expr()
        if len(expr_c) == 2:
            expr1_c, expr2_c = expr_c
        else:
            expr1_c, expr2_c = expr_c[0], None

        op_c: GraphQueryParser.OperatorContext = ctx.operator()

        expr1_r = self.extractExprResult(expr1_c)
        expr2_r = self.extractExprResult(expr2_c)

        op = op_c.accept(self)

        if not isinstance(expr1_r, EpsilonNFA):
            raise Exception(f'Type {type(expr1_r)} is not valid for "{op}" operation')

        if op == "set_final":
            if not isinstance(expr2_r, set):
                raise Exception(
                    f'Type {type(expr2_r)} is not valid for "{op}" operation'
                )
            expr1_r = expr1_r.copy()
            expr1_r.final_states.clear()
            expr1_r.final_states.update(expr2_r)

        elif op == "set_start":
            if not isinstance(expr2_r, set):
                raise Exception(
                    f'Type {type(expr2_r)} is not valid for "{op}" operation'
                )
            expr1_r = expr1_r.copy()
            expr1_r.start_states.clear()
            expr1_r.start_states.update(expr2_r)

        elif op == "add_start":
            if not isinstance(expr2_r, set):
                raise Exception(
                    f'Type {type(expr2_r)} is not valid for "{op}" operation'
                )
            expr1_r = expr1_r.copy()
            expr1_r.start_states.update(expr2_r)

        elif op == "add_final":
            if not isinstance(expr2_r, set):
                raise Exception(
                    f'Type {type(expr2_r)} is not valid for "{op}" operation'
                )
            expr1_r = expr1_r.copy()
            expr1_r.final_states.update(expr2_r)

        elif op == "get_start":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')
            return set(expr1_r.start_states)

        elif op == "get_final":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')
            return set(expr1_r.final_states)

        elif op == "get_reachable":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')

            t: nx.MultiDiGraph = nx.transitive_closure(
                nx.DiGraph(expr1_r.to_networkx())
            )
            return t.edges

        elif op == "get_vertices":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')
            return set(expr1_r.states)

        elif op == "get_edges":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')
            return set(expr1_r)

        elif op == "get_labels":
            if expr2_r is not None:
                raise Exception(f'No argument is needed in "{op}" operation')
            return set(expr1_r.symbols)

        else:
            raise Exception("You should not be here")

        return expr1_r

    def visitIntersect(self, ctx: GraphQueryParser.IntersectContext):
        expr1_c, expr2_c = ctx.expr()
        g1 = self.extractExprResult(expr1_c)
        g2 = self.extractExprResult(expr2_c)

        if isinstance(g1, EpsilonNFA) and isinstance(g2, EpsilonNFA):
            return g1.get_intersection(g2)
        elif isinstance(g1, set) and isinstance(g2, set):
            return g1 & g2
        else:
            raise Exception(
                f"Types {type(g1)} and {type(g2)} are not valid for intersect operation"
            )

    def visitConcat(self, ctx: GraphQueryParser.ConcatContext):
        expr1_c, expr2_c = ctx.expr()
        g1 = self.extractExprResult(expr1_c)
        g2 = self.extractExprResult(expr2_c)

        if isinstance(g1, EpsilonNFA) and isinstance(g2, EpsilonNFA):
            return g1.concatenate(g2)
        elif isinstance(g1, list) and isinstance(g2, list):
            return g1 + g2
        elif isinstance(g1, str) and isinstance(g2, str):
            return g1 + g2
        else:
            raise Exception(
                f"Types {type(g1)} and {type(g2)} are not valid for concat operation"
            )

    def visitUnion(self, ctx: GraphQueryParser.UnionContext):
        expr1_c, expr2_c = ctx.expr()
        g1 = self.extractExprResult(expr1_c)
        g2 = self.extractExprResult(expr2_c)

        if isinstance(g1, EpsilonNFA) and isinstance(g2, EpsilonNFA):
            return g1.union(g2)
        elif isinstance(g1, set) and isinstance(g2, set):
            return g1 | g2
        else:
            raise Exception(
                f"Types {type(g1)} and {type(g2)} are not valid for union operation"
            )

    def visitStar(self, ctx: GraphQueryParser.StarContext):
        expr_c = ctx.expr()
        g = self.extractExprResult(expr_c)

        if not isinstance(g, EpsilonNFA):
            raise Exception(f"Type {type(g)} is not valid for star operation")

        return g.kleene_star()

    def visitVar(self, ctx: GraphQueryParser.VarContext):
        return self.visitChildren(ctx)

    def visitSymb(self, ctx: GraphQueryParser.SymbContext):
        str_c = ctx.STRING()
        symb = str_c.getText()
        result: EpsilonNFA = Regex(symb).to_epsilon_nfa()
        return result

    def visitPrint(self, ctx: GraphQueryParser.PrintContext):
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        expr_r = self.extractExprResult(expr_c)

        if isinstance(expr_r, EpsilonNFA):
            print(nx.nx_pydot.to_pydot(expr_r.to_networkx()).to_string())
        else:
            print(expr_r)

    def visitBind(self, ctx: GraphQueryParser.BindContext):
        id_c: GraphQueryParser.IdContext = ctx.id_()
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        self.vars[id_c.accept(self).value] = self.extractExprResult(expr_c)

    def visitLoad(self, ctx: GraphQueryParser.LoadContext):
        path_c: GraphQueryParser.StringContext = ctx.v()
        return build_NDFA_from_graph(gu.load_graph(path_c.accept(self)))

    def visitMap(self, ctx: GraphQueryParser.MapContext):
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        lambda_c: GraphQueryParser.LambdaContext = ctx.lambda_()

        expr_res = self.extractExprResult(expr_c)

        if Visitor.isIterable(expr_res):
            s = expr_res
        elif isinstance(expr_res, Visitor.ID):
            raise Exception(f'Var "{expr_res.value}" is not found')
        else:
            raise Exception(f'"{type(expr_res)}" is not a valid type for map')

        lam: callable = lambda_c.accept(self)

        return lam(s)

    def visitFilter(self, ctx: GraphQueryParser.FilterContext):
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        lambda_c: GraphQueryParser.LambdaContext = ctx.lambda_()

        expr_res = self.extractExprResult(expr_c)

        if Visitor.isIterable(expr_res):
            s = expr_res
        elif isinstance(expr_res, Visitor.ID):
            raise Exception(f'Var "{expr_res.value}" is not found')
        else:
            raise Exception(f'"{type(expr_res)}" is not a valid type for filter')

        lam: callable = lambda_c.accept(self)

        result = []
        for flag, val in zip(lam(s), s):
            if flag:
                result.append(val)
        return result

    def visitLambda(self, ctx: GraphQueryParser.LambdaContext):
        id_c: GraphQueryParser.IdContext = ctx.id_()
        code_c = ctx.CODE()

        id = id_c.accept(self)
        code = code_c.getText().strip("{{").strip("}}")

        def func(s):
            result = list()
            for i in s:
                context = dict()
                context["__param__"] = i
                exec(
                    f"__result__ = (lambda {id.value}:{code})(__param__)",
                    self.vars,
                    context,
                )
                result.append(context["__result__"])
            return result

        return func

    def visitId(self, ctx: GraphQueryParser.IdContext):
        return Visitor.ID(ctx.getText())

    def visitString(self, ctx: GraphQueryParser.StringContext):
        return ctx.getText()[1:-1]

    def visitInt(self, ctx: GraphQueryParser.IntContext):
        return int(ctx.INT().getText())

    def visitSet(self, ctx: GraphQueryParser.SetContext):
        v_c = ctx.v()

        result = set()
        for c in v_c:
            result.add(c.accept(self))
        return result

    def visitList(self, ctx: GraphQueryParser.ListContext):
        v_c = ctx.v()

        result = list()
        for c in v_c:
            result.append(c.accept(self))
        return result

    def visitOperator(self, ctx: GraphQueryParser.OperatorContext):
        return ctx.getText()

    def visitPar(self, ctx: GraphQueryParser.ParContext):
        return ctx.expr().accept(self)

    def visitSetExpr(self, ctx: GraphQueryParser.SetExprContext):
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        expr_r = self.extractExprResult(expr_c)

        if isinstance(expr_r, Visitor.ID):
            raise Exception(f'Var "{expr_r.value}" is not found')

        if Visitor.isIterable(expr_r):
            # noinspection PyTypeChecker
            return set(expr_r)
        else:
            raise Exception(f'"{type(expr_r)}" can not be converted to set')

    def visitListExpr(self, ctx: GraphQueryParser.ListExprContext):
        expr_c: GraphQueryParser.ExprContext = ctx.expr()
        expr_r = self.extractExprResult(expr_c)

        if isinstance(expr_r, Visitor.ID):
            raise Exception(f'Var "{expr_r.value}" is not found')

        if Visitor.isIterable(expr_r):
            # noinspection PyTypeChecker
            return list(expr_r)
        else:
            raise Exception(f'"{type(expr_r)}" can not be converted to list')


def typing_program(program: str) -> bool:
    try:
        # Создание парсера и дерева разбора
        lexer = GraphQueryLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = GraphQueryParser(stream)
        tree = parser.program()

        # Проверка типов
        visitor = Visitor()
        visitor.visit(tree)
        return True
    except Exception as e:
        print(f"Type error: {e}")
        return False


def exec_program(program: str) -> dict[str, set[tuple]]:
    try:
        # Создание парсера и дерева разбора
        lexer = GraphQueryLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = GraphQueryParser(stream)
        tree = parser.program()

        # Выполнение программы
        visitor = Visitor()
        visitor.visit(tree)

        # Сбор результатов select
        results = {}
        for var, value in visitor.vars.items():
            if isinstance(value, set):
                results[var] = value

        return results
    except Exception as e:
        print(f"Execution error: {e}")
        return {}
