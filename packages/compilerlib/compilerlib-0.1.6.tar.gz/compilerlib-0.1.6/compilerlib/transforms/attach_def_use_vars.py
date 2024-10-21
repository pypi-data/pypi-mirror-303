import ast
from compilerlib.ast_utils import *

class NameVistor(ast.NodeVisitor):
    def __init__(self):
        self.vars = []

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.vars.append(node.id)

    def visit_Call(self, node):
        # Skip visiting the function name and only visit the argument names        
        for arg in node.args:
            self.visit(arg)  # Visit positional arguments
        for kw in node.keywords:
            if kw.value is not None:
                self.visit(kw.value)  # Visit keyword argument values


class AttachDefUseVars(ast.NodeTransformer):
    def visit_Assign(self, node):
        assert isinstance(node.targets[0], ast.Name)
        node.def_vars = [node.targets[0].id]
        visitor = NameVistor()
        visitor.visit(node.value)
        node.use_vars = visitor.vars
        return node

def transform(tree):
    visitor = AttachDefUseVars()
    tree = visitor.visit(tree)
    return tree