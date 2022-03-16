
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON DIVIDE EQUAL EXPONENTIAL FLOATNUMBER LPAREN MINUS MULTIPLY NUMBER PLUS POINT RPAREN WORD\n            term : term DIVIDE factor\n        \n            term : term MULTIPLY factor\n        \n        expression : term\n    \n        expression : expression EXPONENTIAL term\n    \n        expression : expression PLUS term\n    \n        expression : expression MINUS term\n    \n       factor : FLOATNUMBER  \n              |  NUMBER\n              |  LPAREN expression RPAREN\n    \n            term : factor\n        '
    
_lr_action_items = {'FLOATNUMBER':([0,5,6,7,13,14,15,],[3,3,3,3,3,3,3,]),'NUMBER':([0,5,6,7,13,14,15,],[4,4,4,4,4,4,4,]),'LPAREN':([0,5,6,7,13,14,15,],[5,5,5,5,5,5,5,]),'$end':([1,2,3,4,10,11,12,],[0,-10,-7,-8,-1,-2,-9,]),'DIVIDE':([1,2,3,4,9,10,11,12,16,17,18,],[6,-10,-7,-8,6,-1,-2,-9,6,6,6,]),'MULTIPLY':([1,2,3,4,9,10,11,12,16,17,18,],[7,-10,-7,-8,7,-1,-2,-9,7,7,7,]),'RPAREN':([2,3,4,8,9,10,11,12,16,17,18,],[-10,-7,-8,12,-3,-1,-2,-9,-4,-5,-6,]),'EXPONENTIAL':([2,3,4,8,9,10,11,12,16,17,18,],[-10,-7,-8,13,-3,-1,-2,-9,-4,-5,-6,]),'PLUS':([2,3,4,8,9,10,11,12,16,17,18,],[-10,-7,-8,14,-3,-1,-2,-9,-4,-5,-6,]),'MINUS':([2,3,4,8,9,10,11,12,16,17,18,],[-10,-7,-8,15,-3,-1,-2,-9,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,5,13,14,15,],[1,9,16,17,18,]),'factor':([0,5,6,7,13,14,15,],[2,2,10,11,2,2,2,]),'expression':([5,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> term","S'",1,None,None,None),
  ('term -> term DIVIDE factor','term',3,'p_term_div','yacccc.py',15),
  ('term -> term MULTIPLY factor','term',3,'p_term_mult','yacccc.py',21),
  ('expression -> term','expression',1,'p_express_def','yacccc.py',27),
  ('expression -> expression EXPONENTIAL term','expression',3,'p_express_epon','yacccc.py',33),
  ('expression -> expression PLUS term','expression',3,'p_express_plus','yacccc.py',39),
  ('expression -> expression MINUS term','expression',3,'p_express_minus','yacccc.py',45),
  ('factor -> FLOATNUMBER','factor',1,'p_factor_float','yacccc.py',52),
  ('factor -> NUMBER','factor',1,'p_factor_float','yacccc.py',53),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_float','yacccc.py',54),
  ('term -> factor','term',1,'p_term_def','yacccc.py',62),
]
