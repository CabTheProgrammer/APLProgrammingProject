
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALleftPLUSMINUSleftMULTIPLYDIVIDErightUMINUSCOLON DIVIDE EQUAL EXPONENTIAL FLOATNUMBER LPAREN MINUS MULTIPLY NUMBER PLUS POINT RPAREN WORD\n    stmt : WORD EQUAL expression\n    \n    stmt : expression\n    \n        expression  : expression PLUS term\n                    | term PLUS expression\n                    | expression MINUS term\n                    | term MINUS expression\n                    | expression EXPONENTIAL term\n                    | term EXPONENTIAL expression\n                    | expression PLUS expression\n                    | expression MULTIPLY expression\n                    | expression MULTIPLY term\n                    | term MULTIPLY  expression\n                    \n\n\n    \n    expression : WORD\n    \n    expression : MINUS expression %prec UMINUS\n    \n        expression : term\n    \n            term : term DIVIDE factor\n                 | term MULTIPLY factor\n        \n            term : factor\n        \n       factor :  NUMBER\n              |  FLOATNUMBER\n              |  LPAREN expression RPAREN\n    '
    
_lr_action_items = {'WORD':([0,5,9,10,11,14,15,16,17,18,37,],[2,21,21,21,21,21,21,21,21,21,21,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,],[5,-13,12,16,5,-18,-19,-20,5,5,5,5,5,5,5,5,-14,-13,12,12,-9,-3,-5,-7,-10,-11,-4,-6,12,-12,-17,-16,-21,5,-17,]),'NUMBER':([0,5,9,10,11,12,13,14,15,16,17,18,19,37,38,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'FLOATNUMBER':([0,5,9,10,11,12,13,14,15,16,17,18,19,37,38,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'LPAREN':([0,5,9,10,11,12,13,14,15,16,17,18,19,37,38,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,4,6,7,8,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,],[0,-13,-2,-15,-18,-19,-20,-14,-13,-1,-9,-3,-5,-7,-10,-11,-4,-6,-8,-12,-17,-16,-21,-17,]),'EQUAL':([2,],[10,]),'PLUS':([2,3,4,6,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,],[-13,11,15,-18,-19,-20,-14,-13,11,11,-9,-3,-5,-7,-10,-11,-4,-6,11,-12,-17,-16,-21,-17,]),'EXPONENTIAL':([2,3,4,6,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,],[-13,13,17,-18,-19,-20,-14,-13,13,13,-9,-3,-5,-7,-10,-11,-4,-6,13,-12,-17,-16,-21,-17,]),'MULTIPLY':([2,3,4,6,7,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,],[-13,14,18,-18,-19,-20,-14,-13,14,14,14,37,38,38,-10,-11,14,14,14,-12,-17,-16,-21,-17,]),'RPAREN':([4,6,7,8,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,39,],[-15,-18,-19,-20,-14,-13,36,-9,-3,-5,-7,-10,-11,-4,-6,-8,-12,-17,-16,-21,-17,]),'DIVIDE':([4,6,7,8,25,26,27,29,34,35,36,39,],[19,-18,-19,-20,19,19,19,19,-17,-16,-21,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt':([0,],[1,]),'expression':([0,5,9,10,11,14,15,16,17,18,37,],[3,20,22,23,24,28,30,31,32,33,33,]),'term':([0,5,9,10,11,12,13,14,15,16,17,18,37,],[4,4,4,4,25,26,27,29,4,4,4,4,4,]),'factor':([0,5,9,10,11,12,13,14,15,16,17,18,19,37,38,],[6,6,6,6,6,6,6,6,6,6,6,34,35,34,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmt","S'",1,None,None,None),
  ('stmt -> WORD EQUAL expression','stmt',3,'p_stmt_op','yaccc(NEW ONE).py',18),
  ('stmt -> expression','stmt',1,'p_stmt_def','yaccc(NEW ONE).py',25),
  ('expression -> expression PLUS term','expression',3,'p_express_operation','yaccc(NEW ONE).py',32),
  ('expression -> term PLUS expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',33),
  ('expression -> expression MINUS term','expression',3,'p_express_operation','yaccc(NEW ONE).py',34),
  ('expression -> term MINUS expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',35),
  ('expression -> expression EXPONENTIAL term','expression',3,'p_express_operation','yaccc(NEW ONE).py',36),
  ('expression -> term EXPONENTIAL expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',37),
  ('expression -> expression PLUS expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',38),
  ('expression -> expression MULTIPLY expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',39),
  ('expression -> expression MULTIPLY term','expression',3,'p_express_operation','yaccc(NEW ONE).py',40),
  ('expression -> term MULTIPLY expression','expression',3,'p_express_operation','yaccc(NEW ONE).py',41),
  ('expression -> WORD','expression',1,'p_expression_word','yaccc(NEW ONE).py',63),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','yaccc(NEW ONE).py',89),
  ('expression -> term','expression',1,'p_express_def','yaccc(NEW ONE).py',96),
  ('term -> term DIVIDE factor','term',3,'p_term_operation','yaccc(NEW ONE).py',103),
  ('term -> term MULTIPLY factor','term',3,'p_term_operation','yaccc(NEW ONE).py',104),
  ('term -> factor','term',1,'p_term_def','yaccc(NEW ONE).py',117),
  ('factor -> NUMBER','factor',1,'p_factor_def','yaccc(NEW ONE).py',124),
  ('factor -> FLOATNUMBER','factor',1,'p_factor_def','yaccc(NEW ONE).py',125),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_def','yaccc(NEW ONE).py',126),
]
