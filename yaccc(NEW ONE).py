# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from ProjectLex import tokens

names = { }

# Major ERROR when you don't complete an expression. NEEDS TO BE FIXED!!!
# Divide by zero error.
# It doesn't accept negative numbers. Fix this. FIXED!
# Added runtime error checks, aka panic mode recovery
# TODO: Add support for floating point


# def __init__(self, p):
#    self.p[p.WORD] = p


# Yacc stuff starts here for reference

"""
#def p_assign_variables(p):
    ""
            assign : assign EQUAL expression
       ""
    p[0] = p[3]
"""
"""
def p_assign_def(p):
   ""
        assign : WORD
    ""

    p[0] = p[1]
"""


def p_stmt_op(p):
    """
    stmt : WORD '=' expression
    """
    names[p[1]] = p[3]


def p_stmt_def(p):
    """
    stmt : expression
    """
    print(p[1])


def p_express_operation(p):
    """
        expression : expression PLUS term
                    | expression MINUS term
                    | expression EXPONENTIAL term

    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '^':
        p[0] = pow(p[1], p[3])  # This is how you use Exponential in Python!


    # elif len(p) > 4:
        # WordOp(p)


def p_expression_word(p):
    """
    expression : WORD
    """
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s' given!" % p[1])
        p[0] = 0


# This portion of code is defining what has dominance over what sign. Example, '*' has dominance over '-' and '+'
# It is also saying that that Plus and minus have the same level of authority, same with Divide and Multiply
precedence = (

    ('right', 'EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),

)


# Uminus is setting the precedence rule when dealing with negative numbers like '-5' or like '8+5*-3' where you'd
# Either get an error flat out or the compiler/lexer/ yacc thingy would see it as ambiguous and you MIGHT
# NOT GET THE right answer.
def p_expression_uminus(p):
    """
    expression : MINUS expression %prec UMINUS
    """
    p[0] = -p[2]


def p_express_def(p):
    """
        expression : term
    """
    p[0] = p[1]


def p_term_operation(p):
    """
            term : term DIVIDE factor
                  | term MULTIPLY factor
        """
    if p[2] == '/':
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError:
            print("Syntax error! You cannot divide by zero!!!")
    elif p[2] == '*':
        p[0] = p[1] * p[3]


def p_term_def(p):
    """
            term : factor
        """
    p[0] = p[1]

"""
def p_identifier_op(p):
    ""
    identifier : WORD
    ""
    p[0] = p[1]


def p_assign_string(p):
    ""
    assign : identifier '=' expression
            | expression
    ""
    if p[3] == '=':
        p[0] = p[1] = p[3]
    else:
        p[0] = p[1]

def p_assign_def(p):
    ""
    assign : factor
    ""
    p[0] = p[1]
"""


def p_factor_def(p):
    """
       factor :  NUMBER
              |  FLOATNUMBER
              |  PLUS factor
              |  LPAREN expression RPAREN
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


# Function to assign an expression to a variable and save/ calculate the answer. e.g. Base = 5+2
# It works. It calculates the answer, HOWEVER, it still shows an error.
# Maybe due to the placement of the function itself. If you move it more errors might show up lol.
# 'None' shows after an error because it (the pointer/array p[1]) is empty. I think anyway lol.

"""
def p_identifier(p):
    ""

     KEYWORD : IDENTIFIER

        ""
    p[0] = p[1]
"""

"""
class WordOp:
    def p_name_operation(p):
        if p[3] == '+':  # WORD Definition r'[a-zA-Z][a-zA-Z0-9]*' # Int definition r'\d+'   # Float Definition
            # r'\d+\.\d+' # Word Definition [a-zA-Z][a-zA-Z0-9]*
            p[0] = p[2] + p[4]
        elif p[3] == '-':
            p[0] = p[2] + p[4]  # I do believe that this is where we use pointers to manipulate variables etc.
        elif p[3] == '*':
            p[0] = p[2] * p[4]  # Trying to add and print variables.
            print("Your and its calculated is: " +p[4])
        elif p[3] == '/':
            p[0] = p[2] / p[4]
        elif p[4] == '^':
            p[0] = pow(p[2], p[4])
        else:
            p[0] = p[1]
        return p[0]
"""

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
