import ply.yacc as yacc
from streaks_lexer import tokens
from twoWayModel import TwoWayModel

# Diccionario para almacenar las variables
variables = {}

# Definición de la precedencia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE', 'EE'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'POW'),
    ('right', 'NOT'),
)

# Reglas de Producción

# Programa y Lista de Instrucciones
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])
    return execute_statements(p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Instrucción
def p_statement(p):
    '''statement : var_declaration
                 | assignment
                 | if_statement
                 | while_statement
                 | for_statement
                 | print_statement
                 | model_declaration
                 | model_operation
                 | model_operation_with_params
                 | model_assign_r
                 | function_declaration
                 | return_statement
                 | continue_statement
                 | break_statement
                 | variable_query
                 | comment_expression'''
    p[0] = p[1] if p[1] != '\n' else None

# Declaración y Asignación de Variables
def p_var_declaration(p):
    '''var_declaration : VAR IDENTIFIER EQ numvar_expression SEMICOLON
                       | VAR IDENTIFIER EQ bool_expression SEMICOLON
                       | VAR IDENTIFIER EQ string_expression SEMICOLON
                       | VAR IDENTIFIER EQ identifier_expression SEMICOLON
                       | VAR IDENTIFIER EQ array SEMICOLON
                       | VAR IDENTIFIER EQ matrix SEMICOLON
                       | VAR IDENTIFIER EQ matrixs SEMICOLON'''
    variables[p[2]] = evaluate_expression(p[4])
    p[0] = ('var_declaration', p[2], p[4])

def p_assignment(p):
    '''assignment : IDENTIFIER EQ numvar_expression SEMICOLON
                  | IDENTIFIER EQ bool_expression SEMICOLON
                  | IDENTIFIER EQ string_expression SEMICOLON
                  | IDENTIFIER EQ identifier_expression SEMICOLON
                  | IDENTIFIER EQ array SEMICOLON
                  | IDENTIFIER EQ matrix SEMICOLON'''
    variables[p[1]] = evaluate_expression(p[3])
    p[0] = ('assignment', p[1], p[3])

# Consulta de variable
def p_variable_query(p):
    '''variable_query : IDENTIFIER SEMICOLON'''
    value = variables.get(p[1], None)
    p[0] = ('variable_query', p[1], value)

# Condicionales
def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause else_clause'''
    p[0] = ('if_statement', p[3], p[6], p[8], p[9])

def p_elif_clause(p):
    '''elif_clause : ELIF LPAREN condition RPAREN LBRACE statement_list RBRACE elif_clause
                   | empty'''
    if len(p) == 9:
        p[0] = ('elif', p[3], p[6], p[8])
    else:
        p[0] = None

def p_else_clause(p):
    '''else_clause : ELSE LBRACE statement_list RBRACE
                   | empty'''
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

# Bucles
def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('while_statement', p[3], p[6])

def p_for_statement(p):
    '''for_statement : FOR LPAREN for_initialization  condition SEMICOLON for_update RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('for_statement', p[3], p[5], p[7], p[10])

def p_for_initialization(p):
    '''for_initialization : var_declaration'''
    p[0] = p[1]

def p_for_update(p):
    '''for_update : IDENTIFIER EQ numvar_expression
                  | empty'''
    if p[1]:
        variables[p[1]] = evaluate_expression(p[3])
    p[0] = p[1]

# Impresión de Valores
def p_print_statement(p):
    '''print_statement : PRINT LPAREN numvar_expression RPAREN SEMICOLON
                       | PRINT LPAREN bool_expression RPAREN SEMICOLON
                       | PRINT LPAREN string_expression RPAREN SEMICOLON
                       | PRINT LPAREN identifier_expression RPAREN SEMICOLON'''
    print(evaluate_expression(p[3]))
    p[0] = ('print_statement', p[3])

# Modelos y Operaciones con Modelos
def p_model_declaration(p):
    '''model_declaration : MODEL IDENTIFIER EQ LPAREN NUMBER COMMA array COMMA array COMMA matrixs RPAREN SEMICOLON'''
    variables[p[2]] = TwoWayModel(p[5], p[7], p[9], p[11])
    p[0] = ('model_declaration', p[2], p[5], p[7], p[9], p[11])

def p_model_operation(p):
    '''model_operation : IDENTIFIER DOT IDENTIFIER LPAREN RPAREN SEMICOLON'''
    model = variables.get(p[1])
    if isinstance(model, TwoWayModel):
        method = getattr(model, p[3], None)
        if method:
            result = method()
            print(result)
        else:
            print(f"Error: El modelo '{p[1]}' no tiene el método '{p[3]}'")
    else:
        print(f"Error: '{p[1]}' no es un modelo válido")
    p[0] = ('model_operation', p[1], p[3])

def p_model_operation_with_params(p):
    '''model_operation_with_params : IDENTIFIER DOT IDENTIFIER LPAREN param_list RPAREN SEMICOLON'''
    model = variables.get(p[1])
    if isinstance(model, TwoWayModel):
        method = getattr(model, p[3], None)
        if method:
            result = method(*p[5])
            print(result)
        else:
            print(f"Error: El modelo '{p[1]}' no tiene el método '{p[3]}'")
    else:
        print(f"Error: '{p[1]}' no es un modelo válido")
    p[0] = ('model_operation_with_params', p[1], p[3], p[5])

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_param(p):
    '''param : numvar_expression
             | bool_expression
             | string_expression
             | identifier_expression'''
    p[0] = evaluate_expression(p[1])

def p_model_assign_r(p):
    '''model_assign_r : IDENTIFIER DOT IDENTIFIER EQ array SEMICOLON
                      | IDENTIFIER DOT IDENTIFIER EQ matrix SEMICOLON'''
    model = variables.get(p[1])
    if isinstance(model, TwoWayModel) and p[3] == "R":
        model.R = p[5]
        p[0] = ('model_assign_r', p[1], p[3], p[5])
    else:
        print(f"Error: '{p[1]}' no es un modelo válido o '{p[3]}' no es un campo válido")

# Funciones
def p_function_declaration(p):
    '''function_declaration : FUN IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''
    variables[p[2]] = {'type': 'function', 'params': p[4], 'body': p[7]}
    p[0] = ('function_declaration', p[2], p[4], p[7])

def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA IDENTIFIER
                      | IDENTIFIER
                      | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

# Control de Flujo
def p_return_statement(p):
    '''return_statement : RETURN numvar_expression SEMICOLON
                        | RETURN bool_expression SEMICOLON
                        | RETURN string_expression SEMICOLON
                        | RETURN identifier_expression SEMICOLON'''
    p[0] = ('return_statement', p[2])
    return evaluate_expression(p[2])

def p_continue_statement(p):
    '''continue_statement : CONTINUE SEMICOLON'''
    p[0] = 'continue'

def p_break_statement(p):
    '''break_statement : BREAK SEMICOLON'''
    p[0] = 'break'

# Expresiones Numéricas y de Variables
def p_numvar_expression(p):
    '''numvar_expression : numvar_expression PLUS numvar_expression
                         | numvar_expression MINUS numvar_expression
                         | numvar_expression MUL numvar_expression
                         | numvar_expression DIV numvar_expression
                         | numvar_expression POW numvar_expression
                         | numvar'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('arithmetic', p[2], p[1], p[3])

def p_numvar(p):
    '''numvar : NUMBER
              | IDENTIFIER'''
    if isinstance(p[1], int) or isinstance(p[1], float):
        p[0] = p[1]
    else:
        p[0] = variables.get(p[1], 0)

def p_bool_expression(p):
    '''bool_expression : bool_expression AND bool_expression
                       | bool_expression OR bool_expression
                       | NOT bool_expression
                       | BOOL'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('not', p[2])
    else:
        p[0] = ('logical', p[2], p[1], p[3])

def p_comparison_expression(p):
    '''comparison_expression : numvar_expression EQ numvar_expression
                             | numvar_expression NE numvar_expression
                             | numvar_expression EE numvar_expression
                             | numvar_expression LT numvar_expression
                             | numvar_expression LTE numvar_expression
                             | numvar_expression GT numvar_expression
                             | numvar_expression GTE numvar_expression
                             | bool_expression EQ bool_expression
                             | bool_expression NE bool_expression
                             | bool_expression EE bool_expression'''
    p[0] = ('comparison', p[2], p[1], p[3])

def p_string_expression(p):
    '''string_expression : STRING'''
    p[0] = p[1]

def p_identifier_expression(p):
    '''identifier_expression : IDENTIFIER'''
    p[0] = variables.get(p[1], p[1])

def p_condition(p):
    '''condition : comparison_expression
                 | bool_expression'''
    p[0] = p[1]

# Arrays y Matrices
def p_array(p):
    '''array : LBRACKET elements RBRACKET'''
    p[0] = p[2]

def p_elements(p):
    '''elements : elements COMMA numvar_expression
                | numvar_expression
                | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_matrixs(p):
    '''matrixs : LBRACKET matrixs COMMA matrix RBRACKET
               | matrix
               | empty'''
    if len(p) == 6:
        p[0] = p[2] + [p[4]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_matrix(p):
    '''matrix : LBRACKET arrays RBRACKET'''
    p[0] = p[2]

def p_arrays(p):
    '''arrays : arrays COMMA array
              | array
              | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

# Comentarios
def p_comment_expression(p):
    '''comment_expression : COMMENT STRING'''
    pass

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}', line {p.lineno}, type {p.type}")
        # Mostrar el contexto del error, si está disponible
        tok = parser.token()
        while tok is not None:
            if tok.lineno == p.lineno:
                print(f"Context: {tok.value}", end=' ')
            tok = parser.token()
        print()  # Nueva línea después de mostrar el contexto
    else:
        print("Syntax error at EOF (End Of File)")

# Construcción del Parser
parser = yacc.yacc()

def evaluate_condition(condition):
    if isinstance(condition, tuple):
        if condition[0] == 'logical':
            left = evaluate_condition(condition[2])
            right = evaluate_condition(condition[3])
            if condition[1] == 'and':
                return left and right
            elif condition[1] == 'or':
                return left or right
        elif condition[0] == 'comparison':
            left = evaluate_expression(condition[2])
            right = evaluate_expression(condition[3])
            if condition[1] == '==':
                return left == right
            elif condition[1] == '!=':
                return left != right
            elif condition[1] == '<':
                return left < right
            elif condition[1] == '<=':
                return left <= right
            elif condition[1] == '>':
                return left > right
            elif condition[1] == '>=':
                return left >= right
    else:
        return condition

def evaluate_expression(expression):
    if isinstance(expression, tuple):
        if expression[0] == 'arithmetic':
            left = evaluate_expression(expression[2])
            right = evaluate_expression(expression[3])
            if expression[1] == '+':
                return left + right
            elif expression[1] == '-':
                return left - right
            elif expression[1] == '*':
                return left * right
            elif expression[1] == '/':
                return left / right
            elif expression[1] == '^':
                return left ** right
    elif isinstance(expression, list):
        return [evaluate_expression(e) for e in expression]
    else:
        if isinstance(expression, int) or isinstance(expression, float):
            return expression
        return variables.get(expression, expression)

def execute_statements(statements):
    result = None
    for statement in statements:
        if statement:
            if isinstance(statement, tuple):
                if statement[0] == 'var_declaration':
                    variables[statement[1]] = evaluate_expression(statement[2])
                elif statement[0] == 'assignment':
                    variables[statement[1]] = evaluate_expression(statement[2])
                elif statement[0] == 'if_statement':
                    if evaluate_condition(statement[1]):
                        result = execute_statements(statement[2])
                    elif statement[3]:
                        result = execute_statements(statement[3][2])
                    elif statement[4]:
                        result = execute_statements(statement[4][1])
                elif statement[0] == 'while_statement':
                    while evaluate_condition(statement[1]):
                        result = execute_statements(statement[2])
                        if not evaluate_condition(statement[1]):
                            break
                elif statement[0] == 'for_statement':
                    execute_statements([statement[1]])
                    while evaluate_condition(statement[2]):
                        result = execute_statements(statement[4])
                        execute_statements([statement[3]])
                elif statement[0] == 'print_statement':
                    result = evaluate_expression(statement[1])
                    print(result)
                elif statement[0] == 'return_statement':
                    return evaluate_expression(statement[1])
                elif statement[0] == 'break_statement':
                    break
                elif statement[0] == 'continue_statement':
                    continue
                elif statement[0] == 'variable_query':
                    result = f"{statement[1]} = {statement[2]}"
                    print(result)
    return result
