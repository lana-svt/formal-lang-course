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


def count_nodes(tree: ParserRuleContext) -> int:
    if tree is None:
        return 0
    total_nodes = 1
    for child_index in range(tree.getChildCount()):
        total_nodes += count_nodes(tree.getChild(child_index))
    return total_nodes


def convert_tree_to_string(tree: ParserRuleContext) -> str:
    if tree is None:
        return ""
    if tree.getChildCount() == 0:
        return tree.getText()
    children_texts = []
    for child_index in range(tree.getChildCount()):
        children_texts.append(convert_tree_to_string(tree.getChild(child_index)))
    return " ".join(children_texts)
