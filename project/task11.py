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


def nodes_count(tree: ParserRuleContext) -> int:
    class NodeCounterListener(GraphQueryListener):
        def __init__(self) -> None:
            super(GraphQueryListener, self).__init__()
            self.node_count = 0

        def enterEveryRule(self, ctx):
            self.node_count += 1

    node_counter = NodeCounterListener()
    tree.enterRule(node_counter)
    return node_counter.node_count

def tree_to_prog(tree: ParserRuleContext) -> str:
    class ProgramTextListener(GraphQueryListener):
        def __init__(self):
            super(GraphQueryListener, self).__init__()
            self.program_text = ""

        def enterEveryRule(self, ctx):
            self.program_text += ctx.getText()

    program_text_listener = ProgramTextListener()
    tree.enterRule(program_text_listener)
    return program_text_listener.program_text

