from antlr4 import *
from GraphQueryLexer import GraphQueryLexer
from GraphQueryParser import GraphQueryParser


def prog_to_tree(program: str) -> tuple[ParserRuleContext, bool]:
    input_stream = InputStream(program)
    lexer = GraphQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphQueryParser(stream)
    try:
        tree = parser.prog()
        return tree, True
    except Exception as e:
        return None, False


def nodes_count(tree: ParserRuleContext) -> int:
    if tree is None:
        return 0
    count = 1
    for i in range(tree.getChildCount()):
        count += nodes_count(tree.getChild(i))
    return count


def tree_to_prog(tree: ParserRuleContext) -> str:
    if tree is None:
        return ''
    return tree.getText()
