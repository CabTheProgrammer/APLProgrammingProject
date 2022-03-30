# Yacc example
# Done by: Ralph Taylor     |ID: 1803071
#          Seantae Laylor   |ID: 1808021
#          Casandru Bartley |ID: 1808016
import ply.yacc as yacc
from TextToSpeech import *

# Get the token map from the lexer.  This is required.
from ProjectLex import tokens
names = { }

# Major ERROR when you don't complete an expression. NEEDS TO BE FIXED!!!
# Divide by zero error.
# Added runtime error checks, aka panic mode recovery

def p_print_stuff(p):
    """
    OUTPUT : PRINT stmt COMMA WORD
    """
    print("Activated")

    
# def p_string(p):
#     """
#     STRING : QUOTE WORD QUOTE
#     """
#     p[0] = p[2]
#     print(p[2])

#  QUOTE stmt QUOTE
# | WORD EQUAL STRING

def p_stmt_op(p):
    """
    stmt : WORD EQUAL expression  
         | WORD EQUAL STRING
         
    """
    names[p[1]] = p[3]


def p_stmt_def(p):
    """
    stmt : expression
         
    """
    print(p[1])


def p_express_operation(p):
    """
        expression  : expression PLUS term
                    | expression PLUS expression
                    |       term PLUS expression
                    | expression MINUS term
                    |       term MINUS expression
                    | expression MINUS expression
                    | expression EXPONENTIAL term
                    |       term EXPONENTIAL expression
                    | expression EXPONENTIAL expression
                    | expression MULTIPLY term
                    |       term MULTIPLY  expression
                    | expression MULTIPLY expression
                    | expression DIVIDE term
                    |       term DIVIDE expression
                    | expression DIVIDE expression
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '^':
        p[0] = pow(p[1], p[3])  # This is how you use Exponential in Python!
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError:
          p = "Syntax error! Idiot behind keyboard detected!"
          anything(p)

    

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

    ('right', 'EQUAL'), #has the least dominance
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'), # has the most dominance

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
          p = "Syntax error! Idiot behind keyboard detected!"
          anything(p)
    elif p[2] == '*':
        p[0] = p[1] * p[3]


def p_term_def(p):
    """
            term : factor
        """
    p[0] = p[1]


def p_factor_def(p):
    """
       factor :  NUMBER
              |  FLOATNUMBER
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


# Error rule for syntax errors


def p_error(p):
    print("Syntax error at '%s'" % p.value)
    print("This is the last type: " + p.type)
   


# Build the parser
parser = yacc.yacc(debug=True)
# parser = yacc.yacc()

print("Welcome to the SRC programming language\n")
while True:
    try:

        s = input('src > ')
    
        # anything(s);
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    #print(result)
# Done by: Ralph Taylor     |ID: 1803071
#          Seantae Laylor   |ID: 1808021
#          Casandru Bartley |ID: 1808016