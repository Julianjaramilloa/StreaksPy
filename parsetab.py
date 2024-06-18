
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQNEEEleftLTLTEGTGTEleftPLUSMINUSleftMULDIVrightPOWrightNOTAND BOOL BREAK COMMA COMMENT CONTINUE DIV DOT EE ELIF ELSE EQ FOR FUN GT GTE IDENTIFIER IF LBRACE LBRACKET LPAREN LT LTE MINUS MODEL MUL NE NOT NUMBER OR PLUS POW PRINT RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING VAR WHILEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : var_declaration\n                 | assignment\n                 | if_statement\n                 | while_statement\n                 | for_statement\n                 | print_statement\n                 | model_declaration\n                 | model_operation\n                 | model_operation_with_params\n                 | model_assign_r\n                 | function_declaration\n                 | return_statement\n                 | continue_statement\n                 | break_statement\n                 | variable_query\n                 | comment_expressionvar_declaration : VAR IDENTIFIER EQ numvar_expression SEMICOLON\n                       | VAR IDENTIFIER EQ bool_expression SEMICOLON\n                       | VAR IDENTIFIER EQ string_expression SEMICOLON\n                       | VAR IDENTIFIER EQ identifier_expression SEMICOLON\n                       | VAR IDENTIFIER EQ array SEMICOLON\n                       | VAR IDENTIFIER EQ matrix SEMICOLON\n                       | VAR IDENTIFIER EQ matrixs SEMICOLONassignment : IDENTIFIER EQ numvar_expression SEMICOLON\n                  | IDENTIFIER EQ bool_expression SEMICOLON\n                  | IDENTIFIER EQ string_expression SEMICOLON\n                  | IDENTIFIER EQ identifier_expression SEMICOLON\n                  | IDENTIFIER EQ array SEMICOLON\n                  | IDENTIFIER EQ matrix SEMICOLONvariable_query : IDENTIFIER SEMICOLONif_statement : IF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause else_clauseelif_clause : ELIF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause\n                   | emptyelse_clause : ELSE LBRACE statement_list RBRACE\n                   | emptywhile_statement : WHILE LPAREN condition RPAREN LBRACE statement_list RBRACEfor_statement : FOR LPAREN for_initialization  condition SEMICOLON for_update RPAREN LBRACE statement_list RBRACEfor_initialization : var_declarationfor_update : IDENTIFIER EQ numvar_expression\n                  | emptyprint_statement : PRINT LPAREN numvar_expression RPAREN SEMICOLON\n                       | PRINT LPAREN bool_expression RPAREN SEMICOLON\n                       | PRINT LPAREN string_expression RPAREN SEMICOLON\n                       | PRINT LPAREN identifier_expression RPAREN SEMICOLONmodel_declaration : MODEL IDENTIFIER EQ LPAREN NUMBER COMMA array COMMA array COMMA matrixs RPAREN SEMICOLONmodel_operation : IDENTIFIER DOT IDENTIFIER LPAREN RPAREN SEMICOLONmodel_operation_with_params : IDENTIFIER DOT IDENTIFIER LPAREN param_list RPAREN SEMICOLONparam_list : param_list COMMA param\n                  | param\n                  | emptyparam : numvar_expression\n             | bool_expression\n             | string_expression\n             | identifier_expressionmodel_assign_r : IDENTIFIER DOT IDENTIFIER EQ array SEMICOLON\n                      | IDENTIFIER DOT IDENTIFIER EQ matrix SEMICOLONfunction_declaration : FUN IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACEparameter_list : parameter_list COMMA IDENTIFIER\n                      | IDENTIFIER\n                      | emptyreturn_statement : RETURN numvar_expression SEMICOLON\n                        | RETURN bool_expression SEMICOLON\n                        | RETURN string_expression SEMICOLON\n                        | RETURN identifier_expression SEMICOLONcontinue_statement : CONTINUE SEMICOLONbreak_statement : BREAK SEMICOLONnumvar_expression : numvar_expression PLUS numvar_expression\n                         | numvar_expression MINUS numvar_expression\n                         | numvar_expression MUL numvar_expression\n                         | numvar_expression DIV numvar_expression\n                         | numvar_expression POW numvar_expression\n                         | numvarnumvar : NUMBER\n              | IDENTIFIERbool_expression : bool_expression AND bool_expression\n                       | bool_expression OR bool_expression\n                       | NOT bool_expression\n                       | BOOLcomparison_expression : numvar_expression EQ numvar_expression\n                             | numvar_expression NE numvar_expression\n                             | numvar_expression EE numvar_expression\n                             | numvar_expression LT numvar_expression\n                             | numvar_expression LTE numvar_expression\n                             | numvar_expression GT numvar_expression\n                             | numvar_expression GTE numvar_expression\n                             | bool_expression EQ bool_expression\n                             | bool_expression NE bool_expression\n                             | bool_expression EE bool_expressionstring_expression : STRINGidentifier_expression : IDENTIFIERcondition : comparison_expression\n                 | bool_expressionarray : LBRACKET elements RBRACKETelements : elements COMMA numvar_expression\n                | numvar_expression\n                | emptymatrixs : LBRACKET matrixs COMMA matrix RBRACKET\n               | matrix\n               | emptymatrix : LBRACKET arrays RBRACKETarrays : arrays COMMA array\n              | array\n              | emptycomment_expression : COMMENT STRINGempty :'
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,39,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,20,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,20,20,-44,-45,-46,-47,-49,-58,-59,20,20,20,-50,-108,-39,20,-108,-36,20,-60,-34,-38,20,20,-40,20,-37,20,20,-48,-108,-35,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,32,34,35,36,37,38,40,53,54,55,56,63,71,72,78,79,80,81,82,83,84,85,88,89,98,100,101,102,103,104,105,106,112,118,119,120,121,122,123,124,142,143,144,145,146,147,148,149,155,168,179,180,181,182,183,184,187,188,193,195,196,197,198,199,204,209,211,212,214,216,219,221,222,225,226,228,229,230,232,234,236,240,241,244,245,246,247,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,33,41,42,51,-2,51,-33,64,69,69,51,-68,-69,-107,51,69,69,-41,132,-64,69,69,69,69,69,-65,-66,-67,69,-27,-28,-29,-30,-31,-32,69,51,69,69,69,69,69,69,69,-20,-21,-22,-23,-24,-25,-26,69,69,21,21,201,-44,-45,-46,-47,205,69,-49,51,-58,-59,21,21,21,-50,-108,-39,69,21,-108,-36,21,-60,-34,-38,69,21,21,-40,21,-37,21,21,-48,-108,-35,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,22,22,-44,-45,-46,-47,-49,-58,-59,22,22,22,-50,-108,-39,22,-108,-36,22,-60,-34,-38,22,22,-40,22,-37,22,22,-48,-108,-35,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,23,23,-44,-45,-46,-47,-49,-58,-59,23,23,23,-50,-108,-39,23,-108,-36,23,-60,-34,-38,23,23,-40,23,-37,23,23,-48,-108,-35,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,24,24,-44,-45,-46,-47,-49,-58,-59,24,24,24,-50,-108,-39,24,-108,-36,24,-60,-34,-38,24,24,-40,24,-37,24,24,-48,-108,-35,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,25,25,-44,-45,-46,-47,-49,-58,-59,25,25,25,-50,-108,-39,25,-108,-36,25,-60,-34,-38,25,25,-40,25,-37,25,25,-48,-108,-35,]),'MODEL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,26,26,-44,-45,-46,-47,-49,-58,-59,26,26,26,-50,-108,-39,26,-108,-36,26,-60,-34,-38,26,26,-40,26,-37,26,26,-48,-108,-35,]),'FUN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,27,27,-44,-45,-46,-47,-49,-58,-59,27,27,27,-50,-108,-39,27,-108,-36,27,-60,-34,-38,27,27,-40,27,-37,27,27,-48,-108,-35,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,28,28,-44,-45,-46,-47,-49,-58,-59,28,28,28,-50,-108,-39,28,-108,-36,28,-60,-34,-38,28,28,-40,28,-37,28,28,-48,-108,-35,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,29,29,-44,-45,-46,-47,-49,-58,-59,29,29,29,-50,-108,-39,29,-108,-36,29,-60,-34,-38,29,29,-40,29,-37,29,29,-48,-108,-35,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,30,30,-44,-45,-46,-47,-49,-58,-59,30,30,30,-50,-108,-39,30,-108,-36,30,-60,-34,-38,30,30,-40,30,-37,30,30,-48,-108,-35,]),'COMMENT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,168,179,181,182,183,184,193,196,197,198,199,204,209,211,212,216,219,221,222,225,226,228,230,232,234,236,240,241,244,245,246,247,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,31,31,-44,-45,-46,-47,-49,-58,-59,31,31,31,-50,-108,-39,31,-108,-36,31,-60,-34,-38,31,31,-40,31,-37,31,31,-48,-108,-35,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,181,182,183,184,193,196,197,209,211,212,219,221,225,226,228,234,240,245,246,247,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-44,-45,-46,-47,-49,-58,-59,-50,-108,-39,-108,-36,-60,-34,-38,-40,-37,-48,-108,-35,]),'RBRACE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,35,53,54,55,79,85,88,89,100,101,102,103,104,105,142,143,144,145,146,147,148,181,182,183,184,193,196,197,198,199,209,211,212,216,219,221,225,226,228,230,234,236,240,244,245,246,247,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-2,-33,-68,-69,-107,-64,-65,-66,-67,-27,-28,-29,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-44,-45,-46,-47,-49,-58,-59,211,212,-50,-108,-39,225,-108,-36,-60,-34,-38,234,-40,240,-37,246,-48,-108,-35,]),'EQ':([21,33,41,47,49,52,64,67,68,69,90,135,136,137,138,139,140,141,201,],[34,56,77,-75,-81,-76,113,115,118,-77,-80,-70,-71,-72,-73,-74,-78,-79,214,]),'DOT':([21,],[36,]),'SEMICOLON':([21,29,30,43,44,45,46,47,49,50,51,52,56,57,58,59,60,61,62,66,67,69,90,91,92,93,94,95,96,97,99,126,127,128,129,130,135,136,137,138,139,140,141,154,156,158,166,167,169,170,171,172,173,174,175,176,177,178,194,218,242,],[35,53,54,79,85,88,89,-75,-81,-92,-77,-76,-108,100,101,102,103,104,105,-94,-95,-77,-80,142,143,144,145,146,147,148,-102,180,181,182,183,184,-70,-71,-72,-73,-74,-78,-79,-96,-103,193,196,197,-89,-90,-91,-82,-83,-84,-85,-86,-87,-88,209,-100,245,]),'LPAREN':([22,23,24,25,42,64,77,220,],[37,38,39,40,78,112,131,229,]),'NOT':([28,34,37,38,40,48,56,71,72,86,87,112,115,116,117,142,143,144,145,146,147,148,195,229,],[48,48,48,48,48,48,48,48,-41,48,48,48,48,48,48,-20,-21,-22,-23,-24,-25,-26,48,48,]),'BOOL':([28,34,37,38,40,48,56,71,72,86,87,112,115,116,117,142,143,144,145,146,147,148,195,229,],[49,49,49,49,49,49,49,49,-41,49,49,49,49,49,49,-20,-21,-22,-23,-24,-25,-26,49,49,]),'STRING':([28,31,34,40,56,112,195,],[50,55,50,50,50,50,50,]),'NUMBER':([28,34,37,38,40,56,63,71,72,80,81,82,83,84,98,106,112,118,119,120,121,122,123,124,131,142,143,144,145,146,147,148,149,155,188,195,214,229,],[52,52,52,52,52,52,52,52,-41,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,185,-20,-21,-22,-23,-24,-25,-26,52,52,52,52,52,52,]),'LBRACKET':([34,56,63,98,113,149,157,188,190,203,207,224,235,239,],[63,98,106,149,63,188,106,188,207,106,106,106,239,188,]),'PLUS':([43,47,51,52,57,68,69,73,91,109,135,136,137,138,139,162,172,173,174,175,176,177,178,191,223,],[80,-75,-77,-76,80,80,-77,80,80,80,-70,-71,-72,-73,-74,80,80,80,80,80,80,80,80,80,80,]),'MINUS':([43,47,51,52,57,68,69,73,91,109,135,136,137,138,139,162,172,173,174,175,176,177,178,191,223,],[81,-75,-77,-76,81,81,-77,81,81,81,-70,-71,-72,-73,-74,81,81,81,81,81,81,81,81,81,81,]),'MUL':([43,47,51,52,57,68,69,73,91,109,135,136,137,138,139,162,172,173,174,175,176,177,178,191,223,],[82,-75,-77,-76,82,82,-77,82,82,82,82,82,-72,-73,-74,82,82,82,82,82,82,82,82,82,82,]),'DIV':([43,47,51,52,57,68,69,73,91,109,135,136,137,138,139,162,172,173,174,175,176,177,178,191,223,],[83,-75,-77,-76,83,83,-77,83,83,83,83,83,-72,-73,-74,83,83,83,83,83,83,83,83,83,83,]),'POW':([43,47,51,52,57,68,69,73,91,109,135,136,137,138,139,162,172,173,174,175,176,177,178,191,223,],[84,-75,-77,-76,84,84,-77,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'AND':([44,49,58,67,74,90,92,140,141,163,169,170,171,],[86,-81,86,86,86,-80,86,-78,86,86,86,86,86,]),'OR':([44,49,58,67,74,90,92,140,141,163,169,170,171,],[87,-81,87,87,87,-80,87,-78,-79,87,87,87,87,]),'NE':([47,49,52,67,68,69,90,135,136,137,138,139,140,141,],[-75,-81,-76,116,119,-77,-80,-70,-71,-72,-73,-74,-78,-79,]),'EE':([47,49,52,67,68,69,90,135,136,137,138,139,140,141,],[-75,-81,-76,117,120,-77,-80,-70,-71,-72,-73,-74,-78,-79,]),'LT':([47,52,68,69,135,136,137,138,139,],[-75,-76,121,-77,-70,-71,-72,-73,-74,]),'LTE':([47,52,68,69,135,136,137,138,139,],[-75,-76,122,-77,-70,-71,-72,-73,-74,]),'GT':([47,52,68,69,135,136,137,138,139,],[-75,-76,123,-77,-70,-71,-72,-73,-74,]),'GTE':([47,52,68,69,135,136,137,138,139,],[-75,-76,124,-77,-70,-71,-72,-73,-74,]),'RPAREN':([47,49,50,51,52,65,66,67,69,70,73,74,75,76,78,90,99,112,132,133,134,135,136,137,138,139,140,141,151,156,159,160,161,162,163,164,165,169,170,171,172,173,174,175,176,177,178,180,200,202,205,210,218,223,233,235,238,],[-75,-81,-92,-77,-76,114,-94,-95,-77,125,127,128,129,130,-108,-80,-102,158,-62,186,-63,-70,-71,-72,-73,-74,-78,-79,-101,-103,194,-52,-53,-54,-55,-56,-57,-89,-90,-91,-82,-83,-84,-85,-86,-87,-88,-108,213,-43,-61,-51,-100,-42,237,-108,242,]),'RBRACKET':([47,52,63,69,98,106,107,108,109,110,111,135,136,137,138,139,149,152,153,154,156,188,189,191,192,206,207,208,217,239,243,],[-75,-76,-108,-77,-108,-108,154,156,-98,-99,-105,-70,-71,-72,-73,-74,-108,-99,-99,-96,-103,-108,-99,-97,-104,-99,-108,218,-106,-108,-106,]),'COMMA':([47,49,50,51,52,63,69,78,90,98,106,107,108,109,110,111,112,132,133,134,135,136,137,138,139,140,141,149,150,151,152,153,154,156,159,160,161,162,163,164,165,185,188,189,191,192,205,206,207,210,215,217,218,231,239,243,],[-75,-81,-92,-77,-76,-108,-77,-108,-80,-108,-108,155,157,-98,-99,-105,-108,-62,187,-63,-70,-71,-72,-73,-74,-78,-79,-108,190,-101,-99,-99,-96,-103,195,-52,-53,-54,-55,-56,-57,203,-108,-99,-97,-104,-61,-99,-108,-51,224,-106,-100,235,-108,-102,]),'LBRACE':([114,125,186,213,227,237,],[168,179,204,222,232,241,]),'ELIF':([211,246,],[220,220,]),'ELSE':([211,219,221,246,247,],[-108,227,-36,-108,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,168,179,204,222,232,241,],[2,198,199,216,230,236,244,]),'statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[3,32,3,3,32,32,3,32,3,32,3,32,3,32,]),'var_declaration':([0,2,39,168,179,198,199,204,216,222,230,232,236,241,244,],[4,4,72,4,4,4,4,4,4,4,4,4,4,4,4,]),'assignment':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'if_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'while_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'for_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'print_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'model_declaration':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'model_operation':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'model_operation_with_params':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'model_assign_r':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'function_declaration':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'return_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'continue_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'break_statement':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'variable_query':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'comment_expression':([0,2,168,179,198,199,204,216,222,230,232,236,241,244,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'numvar_expression':([28,34,37,38,40,56,63,71,80,81,82,83,84,98,106,112,118,119,120,121,122,123,124,149,155,188,195,214,229,],[43,57,68,68,73,91,109,68,135,136,137,138,139,109,109,162,172,173,174,175,176,177,178,109,191,109,162,223,68,]),'bool_expression':([28,34,37,38,40,48,56,71,86,87,112,115,116,117,195,229,],[44,58,67,67,74,90,92,67,140,141,163,169,170,171,163,67,]),'string_expression':([28,34,40,56,112,195,],[45,59,75,93,164,164,]),'identifier_expression':([28,34,40,56,112,195,],[46,60,76,94,165,165,]),'numvar':([28,34,37,38,40,56,63,71,80,81,82,83,84,98,106,112,118,119,120,121,122,123,124,149,155,188,195,214,229,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'array':([34,56,63,98,113,149,157,188,203,207,224,239,],[61,95,111,111,166,111,192,111,215,111,231,111,]),'matrix':([34,56,98,113,149,188,190,235,239,],[62,96,151,167,151,151,208,151,151,]),'condition':([37,38,71,229,],[65,70,126,233,]),'comparison_expression':([37,38,71,229,],[66,66,66,66,]),'for_initialization':([39,],[71,]),'matrixs':([56,98,149,188,235,239,],[97,150,150,150,238,150,]),'empty':([56,63,78,98,106,112,149,180,188,207,211,219,235,239,246,],[99,110,134,152,153,161,189,202,206,217,221,228,99,243,221,]),'elements':([63,98,106,149,188,],[107,107,107,107,107,]),'arrays':([63,98,149,188,207,239,],[108,108,108,108,108,108,]),'parameter_list':([78,],[133,]),'param_list':([112,],[159,]),'param':([112,195,],[160,210,]),'for_update':([180,],[200,]),'elif_clause':([211,246,],[219,247,]),'else_clause':([219,],[226,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','streaks_parser.py',24),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','streaks_parser.py',29),
  ('statement_list -> statement','statement_list',1,'p_statement_list','streaks_parser.py',30),
  ('statement -> var_declaration','statement',1,'p_statement','streaks_parser.py',38),
  ('statement -> assignment','statement',1,'p_statement','streaks_parser.py',39),
  ('statement -> if_statement','statement',1,'p_statement','streaks_parser.py',40),
  ('statement -> while_statement','statement',1,'p_statement','streaks_parser.py',41),
  ('statement -> for_statement','statement',1,'p_statement','streaks_parser.py',42),
  ('statement -> print_statement','statement',1,'p_statement','streaks_parser.py',43),
  ('statement -> model_declaration','statement',1,'p_statement','streaks_parser.py',44),
  ('statement -> model_operation','statement',1,'p_statement','streaks_parser.py',45),
  ('statement -> model_operation_with_params','statement',1,'p_statement','streaks_parser.py',46),
  ('statement -> model_assign_r','statement',1,'p_statement','streaks_parser.py',47),
  ('statement -> function_declaration','statement',1,'p_statement','streaks_parser.py',48),
  ('statement -> return_statement','statement',1,'p_statement','streaks_parser.py',49),
  ('statement -> continue_statement','statement',1,'p_statement','streaks_parser.py',50),
  ('statement -> break_statement','statement',1,'p_statement','streaks_parser.py',51),
  ('statement -> variable_query','statement',1,'p_statement','streaks_parser.py',52),
  ('statement -> comment_expression','statement',1,'p_statement','streaks_parser.py',53),
  ('var_declaration -> VAR IDENTIFIER EQ numvar_expression SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',58),
  ('var_declaration -> VAR IDENTIFIER EQ bool_expression SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',59),
  ('var_declaration -> VAR IDENTIFIER EQ string_expression SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',60),
  ('var_declaration -> VAR IDENTIFIER EQ identifier_expression SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',61),
  ('var_declaration -> VAR IDENTIFIER EQ array SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',62),
  ('var_declaration -> VAR IDENTIFIER EQ matrix SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',63),
  ('var_declaration -> VAR IDENTIFIER EQ matrixs SEMICOLON','var_declaration',5,'p_var_declaration','streaks_parser.py',64),
  ('assignment -> IDENTIFIER EQ numvar_expression SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',69),
  ('assignment -> IDENTIFIER EQ bool_expression SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',70),
  ('assignment -> IDENTIFIER EQ string_expression SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',71),
  ('assignment -> IDENTIFIER EQ identifier_expression SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',72),
  ('assignment -> IDENTIFIER EQ array SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',73),
  ('assignment -> IDENTIFIER EQ matrix SEMICOLON','assignment',4,'p_assignment','streaks_parser.py',74),
  ('variable_query -> IDENTIFIER SEMICOLON','variable_query',2,'p_variable_query','streaks_parser.py',80),
  ('if_statement -> IF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause else_clause','if_statement',9,'p_if_statement','streaks_parser.py',86),
  ('elif_clause -> ELIF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause','elif_clause',8,'p_elif_clause','streaks_parser.py',90),
  ('elif_clause -> empty','elif_clause',1,'p_elif_clause','streaks_parser.py',91),
  ('else_clause -> ELSE LBRACE statement_list RBRACE','else_clause',4,'p_else_clause','streaks_parser.py',98),
  ('else_clause -> empty','else_clause',1,'p_else_clause','streaks_parser.py',99),
  ('while_statement -> WHILE LPAREN condition RPAREN LBRACE statement_list RBRACE','while_statement',7,'p_while_statement','streaks_parser.py',107),
  ('for_statement -> FOR LPAREN for_initialization condition SEMICOLON for_update RPAREN LBRACE statement_list RBRACE','for_statement',10,'p_for_statement','streaks_parser.py',111),
  ('for_initialization -> var_declaration','for_initialization',1,'p_for_initialization','streaks_parser.py',115),
  ('for_update -> IDENTIFIER EQ numvar_expression','for_update',3,'p_for_update','streaks_parser.py',119),
  ('for_update -> empty','for_update',1,'p_for_update','streaks_parser.py',120),
  ('print_statement -> PRINT LPAREN numvar_expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','streaks_parser.py',127),
  ('print_statement -> PRINT LPAREN bool_expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','streaks_parser.py',128),
  ('print_statement -> PRINT LPAREN string_expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','streaks_parser.py',129),
  ('print_statement -> PRINT LPAREN identifier_expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','streaks_parser.py',130),
  ('model_declaration -> MODEL IDENTIFIER EQ LPAREN NUMBER COMMA array COMMA array COMMA matrixs RPAREN SEMICOLON','model_declaration',13,'p_model_declaration','streaks_parser.py',136),
  ('model_operation -> IDENTIFIER DOT IDENTIFIER LPAREN RPAREN SEMICOLON','model_operation',6,'p_model_operation','streaks_parser.py',141),
  ('model_operation_with_params -> IDENTIFIER DOT IDENTIFIER LPAREN param_list RPAREN SEMICOLON','model_operation_with_params',7,'p_model_operation_with_params','streaks_parser.py',155),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','streaks_parser.py',169),
  ('param_list -> param','param_list',1,'p_param_list','streaks_parser.py',170),
  ('param_list -> empty','param_list',1,'p_param_list','streaks_parser.py',171),
  ('param -> numvar_expression','param',1,'p_param','streaks_parser.py',180),
  ('param -> bool_expression','param',1,'p_param','streaks_parser.py',181),
  ('param -> string_expression','param',1,'p_param','streaks_parser.py',182),
  ('param -> identifier_expression','param',1,'p_param','streaks_parser.py',183),
  ('model_assign_r -> IDENTIFIER DOT IDENTIFIER EQ array SEMICOLON','model_assign_r',6,'p_model_assign_r','streaks_parser.py',187),
  ('model_assign_r -> IDENTIFIER DOT IDENTIFIER EQ matrix SEMICOLON','model_assign_r',6,'p_model_assign_r','streaks_parser.py',188),
  ('function_declaration -> FUN IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE','function_declaration',8,'p_function_declaration','streaks_parser.py',198),
  ('parameter_list -> parameter_list COMMA IDENTIFIER','parameter_list',3,'p_parameter_list','streaks_parser.py',203),
  ('parameter_list -> IDENTIFIER','parameter_list',1,'p_parameter_list','streaks_parser.py',204),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','streaks_parser.py',205),
  ('return_statement -> RETURN numvar_expression SEMICOLON','return_statement',3,'p_return_statement','streaks_parser.py',215),
  ('return_statement -> RETURN bool_expression SEMICOLON','return_statement',3,'p_return_statement','streaks_parser.py',216),
  ('return_statement -> RETURN string_expression SEMICOLON','return_statement',3,'p_return_statement','streaks_parser.py',217),
  ('return_statement -> RETURN identifier_expression SEMICOLON','return_statement',3,'p_return_statement','streaks_parser.py',218),
  ('continue_statement -> CONTINUE SEMICOLON','continue_statement',2,'p_continue_statement','streaks_parser.py',223),
  ('break_statement -> BREAK SEMICOLON','break_statement',2,'p_break_statement','streaks_parser.py',227),
  ('numvar_expression -> numvar_expression PLUS numvar_expression','numvar_expression',3,'p_numvar_expression','streaks_parser.py',232),
  ('numvar_expression -> numvar_expression MINUS numvar_expression','numvar_expression',3,'p_numvar_expression','streaks_parser.py',233),
  ('numvar_expression -> numvar_expression MUL numvar_expression','numvar_expression',3,'p_numvar_expression','streaks_parser.py',234),
  ('numvar_expression -> numvar_expression DIV numvar_expression','numvar_expression',3,'p_numvar_expression','streaks_parser.py',235),
  ('numvar_expression -> numvar_expression POW numvar_expression','numvar_expression',3,'p_numvar_expression','streaks_parser.py',236),
  ('numvar_expression -> numvar','numvar_expression',1,'p_numvar_expression','streaks_parser.py',237),
  ('numvar -> NUMBER','numvar',1,'p_numvar','streaks_parser.py',244),
  ('numvar -> IDENTIFIER','numvar',1,'p_numvar','streaks_parser.py',245),
  ('bool_expression -> bool_expression AND bool_expression','bool_expression',3,'p_bool_expression','streaks_parser.py',252),
  ('bool_expression -> bool_expression OR bool_expression','bool_expression',3,'p_bool_expression','streaks_parser.py',253),
  ('bool_expression -> NOT bool_expression','bool_expression',2,'p_bool_expression','streaks_parser.py',254),
  ('bool_expression -> BOOL','bool_expression',1,'p_bool_expression','streaks_parser.py',255),
  ('comparison_expression -> numvar_expression EQ numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',264),
  ('comparison_expression -> numvar_expression NE numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',265),
  ('comparison_expression -> numvar_expression EE numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',266),
  ('comparison_expression -> numvar_expression LT numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',267),
  ('comparison_expression -> numvar_expression LTE numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',268),
  ('comparison_expression -> numvar_expression GT numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',269),
  ('comparison_expression -> numvar_expression GTE numvar_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',270),
  ('comparison_expression -> bool_expression EQ bool_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',271),
  ('comparison_expression -> bool_expression NE bool_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',272),
  ('comparison_expression -> bool_expression EE bool_expression','comparison_expression',3,'p_comparison_expression','streaks_parser.py',273),
  ('string_expression -> STRING','string_expression',1,'p_string_expression','streaks_parser.py',277),
  ('identifier_expression -> IDENTIFIER','identifier_expression',1,'p_identifier_expression','streaks_parser.py',281),
  ('condition -> comparison_expression','condition',1,'p_condition','streaks_parser.py',285),
  ('condition -> bool_expression','condition',1,'p_condition','streaks_parser.py',286),
  ('array -> LBRACKET elements RBRACKET','array',3,'p_array','streaks_parser.py',291),
  ('elements -> elements COMMA numvar_expression','elements',3,'p_elements','streaks_parser.py',295),
  ('elements -> numvar_expression','elements',1,'p_elements','streaks_parser.py',296),
  ('elements -> empty','elements',1,'p_elements','streaks_parser.py',297),
  ('matrixs -> LBRACKET matrixs COMMA matrix RBRACKET','matrixs',5,'p_matrixs','streaks_parser.py',306),
  ('matrixs -> matrix','matrixs',1,'p_matrixs','streaks_parser.py',307),
  ('matrixs -> empty','matrixs',1,'p_matrixs','streaks_parser.py',308),
  ('matrix -> LBRACKET arrays RBRACKET','matrix',3,'p_matrix','streaks_parser.py',317),
  ('arrays -> arrays COMMA array','arrays',3,'p_arrays','streaks_parser.py',321),
  ('arrays -> array','arrays',1,'p_arrays','streaks_parser.py',322),
  ('arrays -> empty','arrays',1,'p_arrays','streaks_parser.py',323),
  ('comment_expression -> COMMENT STRING','comment_expression',2,'p_comment_expression','streaks_parser.py',333),
  ('empty -> <empty>','empty',0,'p_empty','streaks_parser.py',337),
]
