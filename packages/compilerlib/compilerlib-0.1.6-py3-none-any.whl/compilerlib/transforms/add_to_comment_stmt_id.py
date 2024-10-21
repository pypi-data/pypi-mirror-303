import ast
from compilerlib.ast_utils import *
from . import attach_id_to_assigns

class AppendCommentStmtId(ast.NodeTransformer):
    def visit_Assign(self, node):
        if node.type_comment is None:
            node.type_comment = '{}'

        comment_dict = ast.literal_eval(node.type_comment)
        comment_dict['stmt_id'] = node.stmt_id
        node.type_comment = str(comment_dict)
        return node

def transform(tree):
    tree = attach_id_to_assigns.transform(tree)
    return AppendCommentStmtId().visit(tree)