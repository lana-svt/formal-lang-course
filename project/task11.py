from antlr4 import *
from antlr4.InputStream import InputStream
from project.GraphQueryLexer import GraphQueryLexer
from project.GraphQueryParser import GraphQueryParser
from project.GraphQueryVisitor import GraphQueryVisitor


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    lexer = GraphQueryLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphQueryParser(stream)
    tree = parser.prog()
    return tree, parser.getNumberOfSyntaxErrors() == 0


def nodes_count(tree: ParserRuleContext) -> int:
    count = 0

    def enterEveryRule(ctx):
        nonlocal count
        count += 1

    walker = ParseTreeWalker()
    listener = make_listener(enterEveryRule)
    walker.walk(listener, tree)
    return count


def tree_to_prog(tree: ParserRuleContext) -> str:
    progText = ""

    def enterEveryRule(ctx):
        nonlocal progText
        progText += ctx.getText()

    walker = ParseTreeWalker()
    listener = make_listener(enterEveryRule)
    walker.walk(listener, tree)
    return progText


def make_listener(enterEveryRule):
    def enterRule(ctx):
        enterEveryRule(ctx)

    listener = ParseTreeListener()
    listener.enterEveryRule = enterRule
    return listener
