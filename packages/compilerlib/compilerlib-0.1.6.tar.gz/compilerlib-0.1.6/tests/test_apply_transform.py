import inspect
from compilerlib.types import *
from compilerlib import *

def foo(a: Array(2), b: Array(2), r: Array(2), iters: int):
    for i in range(iters):
        b = r @ (1.0 / (a @ b))
    return b
    
#print(apply_transform_on_ast('OpToCall', inspect.getsource(foo)))
tree = func_to_ast(foo)
tree = apply_transform_on_ast("to_single_op_form", tree)
tree = apply_transform_on_ast("replace_op_with_call", tree)
tree = apply_transform_on_ast("attach_id_to_assigns", tree)
tree = apply_transform_on_ast("attach_def_use_vars", tree)
tree = apply_transform_on_ast("show_info_in_comment", tree)
print(ast_to_code(tree))