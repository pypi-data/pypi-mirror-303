import ast
import inspect
import importlib

def compile(f):
    '''
    Compiles a function with type annotations. `f` will be compiled before it's used.
    '''
    

def jit(f):
    '''
    Compiles a function with type annotations. `f` is compiled upon its first invocation.
    '''

def apply_transform(transform, f):
    src = inspect.getsource(f)
    tree = ast.parse(src).body[0]
    tree = transform().visit(tree)
    newsrc = ast.unparse(tree)
    local_scope = {}
    exec(newsrc, {}, local_scope)
    return local_scope[f.__name__]

def apply_transform_on_src(transform, src):
    if isinstance(transform, ast.NodeTransformer):
        visitor = transform()
    elif isinstance(transform, str):
        module_name = f"compilerlib.transforms.{transform}"
        module = importlib.import_module(module_name)
        cls = getattr(module, transform)
        visitor = cls()

    tree = ast.parse(src).body[0]
    tree = visitor.visit(tree)
    newsrc = ast.unparse(tree)
    return newsrc