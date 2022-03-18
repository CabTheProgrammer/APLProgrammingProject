# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from ProjectLex import tokens


# Major ERROR when you don't complete an expression. NEEDS TO BE FIXED!!!

# TODO: Add support for floating point


# def __init__(self, p):
#    self.p[p.WORD] = p


def p_express_plus(p):
    """
        expression : expression PLUS term
                    | factor PLUS factor
    """
    p[0] = p[1] + p[3]


def p_term_div(p):
    """
            term : term DIVIDE factor
        """
    p[0] = p[1] / p[3]


def p_term_mult(p):
    """
            term : term MULTIPLY factor
        """
    p[0] = p[1] * p[3]


def p_express_epon(p):
    """
        expression : expression EXPONENTIAL term
    """
    p[0] = pow(p[1], p[3])  # This is how you use Exponential in Python!


def p_express_minus(p):
    """
        expression : expression MINUS term
    """
    p[0] = p[1] - p[3]


# Yacc stuff starts here for reference

# Function to assign an expression to a variable and save/ calculate the answer. e.g. Base = 5+2
# It works. It calculates the answer, HOWEVER, it still shows an error.
# Maybe due to the placement of the function itself. If you move it more errors might show up lol.
# 'None' shows after an error because it (the pointer/array p[1]) is empty. I think anyway lol.
def p_var_operation(p):
    """
    variable : WORD EQUAL expression PLUS term
               | WORD EQUAL expression MINUS term
               | WORD EQUAL expression MULTIPLY term
               | WORD EQUAL expression DIVIDE term
               | WORD EQUAL expression EXPONENTIAL term
               | WORD
    """
    if p[4] == '+':  # WORD Definition r'[a-zA-Z][a-zA-Z0-9]*' # Int definition r'\d+'   # Float Definition
        # r'\d+\.\d+' # Word Definition [a-zA-Z][a-zA-Z0-9]*
        p[0] = p[3] + p[4]
    elif p[4] == '-':
        p[0] = p[3] + p[4]  # I do believe that this is where we use pointers to manipulate variables etc.
    elif p[4] == '*':
        p[0] = p[3] * p[4]
    elif p[4] == '/':
        p[0] = p[3] / p[4]
    elif p[4] == '^':
        p[0] = pow(p[3], p[4])
    else:
        p[0] = p[1]


def p_express_def(p):
    """
        expression : term
    """
    p[0] = p[1]


def p_term_def(p):
    """
            term : factor
        """
    p[0] = p[1]


def p_factor_float(p):
    """
       factor :  NUMBER
              |  FLOATNUMBER
    """
    p[0] = p[1]


def p_factor_expression(p):
    """
        factor : LPAREN expression RPAREN
    """
    p[0] = p[2]


# Yacc stuff ends here for reference


# def p_factor_point(p):
#     'factor : factor POINT'
#     p[0] = p[1]    

# def p_factor_float(p):
#     'factor : FLOATNUMBER'
#     p[0] = p[1]   

# def p_factor_number(p):
#     'factor : NUMBER'
#     p[0] = p[1]

# def p_factor_colon(p):
#     'factor : expression COLON'
#     p[0] = p[2]


# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]

# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]

# def p_term_multiply(p):
#     'term : term MULTIPLY factor'
#     p[0] = p[1] * p[3]

# def p_term_divide(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]

# def p_expression_exponential(p):
#     'expression : expression EXPONENTIAL term'
#     p[0] = p[1] ^ p[3]

# def p_expression_equal(p):
#     'expression : expression EQUAL term'
#     p[0] = p[1] == p[3]

# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]

# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")
    print("This is the last type: " + p.type)


# Build the parser
parser = yacc.yacc(debug=True)

print("Welcome to the SRC programming language\n")
while True:
    try:

        s = input('src > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
