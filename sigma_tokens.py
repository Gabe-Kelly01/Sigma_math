'''
Constant definitions for the tokenizer
DO NOT REMOVE/EDIT TOKENS UNLESS YOU ARE ADDING NEW ONES
'''

# Token types, values map onto the tuple of XML tags
TK_OPERATION = 1
TK_VARIABLE = 2
TK_VALUE = 3
TK_CONSTANT = 4
TK_EXPRESSION = 5
TK_TERM = 6
TK_BINARY_OP = 7
TK_FUNCTOR = 8
TK_CONSTRAINT = 9

tokenTypes = ('<fucked up>', '<operation>', '<variable>', '<value>', '<constant>', '<expression>',
             '<term>','<binary_op>', '<functor>', '<constraint>')

# Operations
OP_SUM = 1
OP_INTEGRATE = 2
OP_EVALUATE = 3
OP_SOLVE = 4
OP_LIMIT = 5
OP_DERIVATIVE = 6
OP_IS = 7

# Constants
CONST_PI = 1
CONST_E = 2
CONST_GOLDENRATIO = 3
CONST_GRAV = 4

# Binary ops
BOP_ADD = 1
BOP_SUB = 2
BOP_MULT = 3
BOP_DIV = 4

# Functors
FUNC_FRAC = 1
FUNC_SQRT = 2
FUNC_LOG = 3
FUNC_MODULO = 4
FUNC_FLOOR = 5
FUNC_CEIL = 6
FUNC_ABS = 7
FUNC_SIN = 8
FUNC_COS = 9
FUNC_TAN = 10
FUNC_ARCSIN = 11
FUNC_ARCCOS = 12
FUNC_ARCTAN = 13