from antlr4 import *
from antlr4.InputStream import InputStream
from project.GraphQueryLexer import GraphQueryLexer
from project.GraphQueryParser import GraphQueryParser
from project.GraphQueryVisitor import GraphQueryVisitor
from project.GraphQueryListener import GraphQueryListener


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    lexer = GraphQueryLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphQueryParser(stream)
    tree = parser.prog()
    return tree, parser.getNumberOfSyntaxErrors() == 0


def nodes_count(parse_tree: ParserRuleContext) -> int:
    class NodeCounter(GraphQueryListener):
        def __init__(self) -> None:
            super(GraphQueryListener, self).__init__()
            self.node_count = 0

        def enterEveryRule(self, ctx):
            self.node_count += 1

    node_counter = NodeCounter()
    walker = ParseTreeWalker()
    walker.walk(node_counter, parse_tree)
    return node_counter.node_count


def tree_to_prog(parse_tree: ParserRuleContext) -> str:
    class TextCollector(GraphQueryListener):
        def __init__(self):
            super(GraphQueryListener, self).__init__()
            self.collected_text = ""

        def enterEveryRule(self, ctx):
            self.collected_text += ctx.getText()

    text_collector = TextCollector()
    walker = ParseTreeWalker()
    walker.walk(text_collector, parse_tree)
    return text_collector.collected_text
