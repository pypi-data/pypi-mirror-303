import ast

class AttachIdToAssigns(ast.NodeTransformer):
    def __init__(self):
        self.count = 0

    def visit_Assign(self, node):
        node.stmt_id = self.count
        self.count += 1
        return node

def transform(tree):
    return AttachIdToAssigns().visit(tree)