# Program to make a lexical Analyzer
# Done by: Ralph Taylor | ID: 1803071

import ply.lex as lex
import sys
# Imports for LEX to make a lexical analyzer

tokens = (

    'WORD',
    'POINT',
    'NUMBER',
    'FLOATNUMBER',
    'COLON',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'EXPONENTIAL',
    'EQUAL',
    'LPAREN',
    'RPAREN',

)

# Regular expression rules for simple tokens

t_POINT = r'\.'
t_PLUS = r'\+'
t_COLON = r'\:'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EXPONENTIAL = r'\^'
t_EQUAL = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

"""
    # If statement to check ig there is a decimal point in the number. If there is it goes to the while loop.

    if t.value != None and t.value + '.':
        while t.value != None and t.value != ' ':

            # While loop is to continue going through the float to the last digit behind the point.
            # Before it recognized it but stopped at the 3.0 and didn't get to the 3.04

            t.value = float(t.value)
            print("Code is here!")
            return t
    # When it breaks, it shows/returns the full number
    else:
"""
#Comments end here.
#Float checker isn't working as yet, but Int or Numbers checking works!


# Regular Expression to obtain/check for Floating point numbers

def t_FLOATNUMBER(t):
    r'^[-+]?[0-9]*[.][0-9]+$'
    #r'[\d]+[.]+[\d]+'
    t.value = float(t.value)
    return t

def t_COMMENT(t):
     r'\#.*'
     pass

 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)



    # r'\d.d+'
    # t.value = float(t.value)
    # return t


# To track line numbers
def t_NewLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# To specify characters/letters (Basically any word)
def t_WORD(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    # THIS DEF NAME MUST MATCH THE PRE-DEFINED TOKEN FROM ABOVE FOR IT TO WORK. SEE LINE 10.
    # So you get t_WORD (Where 't' means Token).
    t.value = str(t.value)

    # Return gives back the WORD TOKEN entered then "Stores it" (I think anyway for the stores part).
    return t


# To tell what to ignore (Space and tabs)
t_ignore = ' \t'


# For error handling
def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)


# To test it out
# PRE-ENTERED DATA
data = ''' 3 + 4  Equals (=) 7  
     '''
# To build the lexer
lexer = lex.lex()

# Give the lexer the data above as input
lexer.input(sys.argv[1]) # you can pass data here to test it with the above string in case 

# Tokenizing it
while True:
    tok = lexer.token()
    if not tok:
        # No more input
        break
    print(tok.type, ": ", tok.value)  # , tok.lineno, tok.lexpos)

# The above is commented, because when YACC is implemented it will accept user input seemingly.

# A for loop may be used instead!
# for token in lexer:
#   print(tok.type, ": ", tok.value) or print(token)

# Program to make a lexical Analyzer
# Done by: Ralph Taylor | ID: 1803071
