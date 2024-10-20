import ast

def new_call(func: str, args: list):
    ret = ast.Call(func = ast.Name(func, ast.Load()), args = args, keywords = [])
    return ret