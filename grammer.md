'variable : WORD'✅

//'factor : factor POINT'
'factor: FLOATNUMBER ✅
        |'NUMBER✅
        | LPAREN expression RPAREN'✅

//'factor : expression COLON'
'term: factor'✅
'expression : expression PLUS term'✅
'expression : expression MINUS term'✅
'term : term MULTIPLY factor'    ✅
'term : term DIVIDE factor'✅


'expression : expression EXPONENTIAL term' ✅
//'expression : expression EQUAL term' 
'expression : term'✅




