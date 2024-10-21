import ast
from compilerlib.ast_utils import *

class AddToCommentStmtId(ast.NodeTransformer):
    def visit_Assign(self, node):
        if not hasattr(node, 'stmt_id'):
            return node

        if node.type_comment is None:
            node.type_comment = '{}'

        comment_dict = ast.literal_eval(node.type_comment)
        comment_dict['stmt_id'] = node.stmt_id
        node.type_comment = str(comment_dict)
        return node


class AddToCommentDefUseVars(ast.NodeTransformer):
    def visit_Assign(self, node):
        if not hasattr(node, 'def_vars'):
            assert not hasattr(node, 'use_vars')
            return node

        if node.type_comment is None:
            node.type_comment = '{}'

        comment_dict = ast.literal_eval(node.type_comment)
        comment_dict['def_vars'] = node.def_vars
        comment_dict['use_vars'] = node.use_vars
        node.type_comment = str(comment_dict)
        return node


def transform(tree):
    tree = AddToCommentStmtId().visit(tree)
    tree = AddToCommentDefUseVars().visit(tree)
    return tree