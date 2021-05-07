import string
from sigma_tokens import *

symbols = '(){}[];,.+-*/|<>='
numberChars = string.digits
variableChars = string.ascii_letters

operations = {
            "sum" : OP_SUM,
            "integrate" : OP_INTEGRATE,
            "evaluate" : OP_EVALUATE,
            "solve" : OP_SOLVE,
            "limit" : OP_LIMIT,
            "derivative" : OP_DERIVATIVE,
            "is" : OP_IS
            }

constants = {
            "pi" : CONST_PI,
            "e" : CONST_E,
            "phi" : CONST_GOLDENRATIO,
            "G" : CONST_GRAV,
            }

binaryOps = {
            "+" : BOP_ADD,
            "-" : BOP_SUB,
            "*" : BOP_MULT,
            "/" : BOP_DIV
            }

functors = {
           "/" : FUNC_FRAC,
           "sqrt": FUNC_SQRT,
           "ln" : FUNC_LN,
           "mod" : FUNC_MODULO,
           "floor" : FUNC_FLOOR,
           "ceil" : FUNC_CEIL,
           "|" : FUNC_ABS,
           "sin" : FUNC_SIN,
           "cos" : FUNC_COS,
           "tan" : FUNC_TAN,
           "arcsin" : FUNC_ARCSIN,
           "arccos" : FUNC_ARCCOS,
           "arctan" : FUNC_ARCTAN 
           }