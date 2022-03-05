# this file will contain the rules for the tokens of our language
# lexer i think should be called

from ply import lex, yacc

tokens =[
    'PLUS'
]


t_PLUS = r'\+'

# Prints error message when the lexer encounters an error
def t_error(t): 
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


# This function keeps track of each line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    