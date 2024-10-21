import ast

class InsertManualAlloc(ast.NodeTransformer):
    

def transform(tree):
    return InsertManualAlloc().visit(tree)
