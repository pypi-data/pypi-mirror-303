import ast
from compilerlib.ast_utils import *

class OpToCall(ast.NodeTransformer):
    def visit_BinOp(self, node):
        newleft = self.visit(node.left)
        newright = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return new_call('add', [newleft, newright])
        elif isinstance(node.op, ast.Sub):
            return new_call('sub', [newleft, newright])
        elif isinstance(node.op, ast.Mult):
            return new_call('mul', [newleft, newright])
        elif isinstance(node.op, ast.Div):
            return new_call('div', [newleft, newright])
        else:
            return node

    def visit_UnaryOp(self, node):
        if node.op in ['neg']:
            return ast.Call(func=ast.Name(id=node.op, ctx=ast.Load()), args=[node.operand], keywords=[])
        else:
            return node