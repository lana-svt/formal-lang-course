from antlr4 import *
from antlr4.InputStream import InputStream
from project.GraphQueryLexer import GraphQueryLexer
from project.GraphQueryParser import GraphQueryParser


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    lexer = GraphQueryLexer(InputStream(program))
    stream = CommonTokenStream(lexer)
    parser = GraphQueryParser(stream)
    tree = parser.prog()
    return tree, parser.getNumberOfSyntaxErrors() == 0


def nodes_count(tree: ParserRuleContext) -> int:
    if not tree:
        return 0
    count = 1
    for i in range(tree.getChildCount()):
        count += nodes_count(tree.getChild(i))
    return count

def tree_to_prog(tree: ParserRuleContext) -> str:
    if not tree:
        return ""
    if tree.getChildCount() == 0:
        return tree.getText()
    result = ""
    for i in range(tree.getChildCount()):
        result += tree_to_prog(tree.getChild(i)) + " "
    return result.strip()
