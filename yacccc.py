# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from ProjectLex import tokens

#TODO: Add support for floating point
# def p_var_word(p):
#     'variable : WORD'
#     p[0] = p[1]

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

def p_express_def(p):
    """
        expression : term
    """
    p[0] = p[1]

def p_express_epon(p):
    """
        expression : expression EXPONENTIAL term
    """
    p[0] = p[1] ^ p[3]

def p_express_plus(p):
    """
        expression : expression PLUS term
    """
    p[0] = p[1] + p[3]

def p_express_minus (p):
    """
        expression : expression MINUS term
    """
    p[0] = p[1] - p[3]


def p_factor_float(p):
    """
       factor : FLOATNUMBER  
              |  NUMBER
              |  LPAREN expression RPAREN
    """
    p[0] = p[1]   



def p_term_def(p):
        """
            term : factor
        """
        p[0] = p[1]


    

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
    print("This is the last type: "+p.type)

# Build the parser
parser = yacc.yacc(debug=True)

print("Welcone to the src programming language\n")
while True:
    try:
       
        s = input('src > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)