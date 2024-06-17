import ply.lex as lex

# Definición de tokens
tokens = (
    # Tipos de datos y valores
    'NUMBER', 'BOOL', 'STRING', 'IDENTIFIER',

    # Operadores lógicos
    'AND', 'OR', 'NOT',

    # Operadores aritméticos
    'PLUS', 'MINUS', 'MUL', 'DIV', 'POW',

    # Operadores de comparación
    'EQ', 'NE', 'EE', 'LT', 'GT', 'LTE', 'GTE',

    # Símbolos y otros
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',

    # Signos de puntuación
    'COMMA', 'SEMICOLON', 'DOT', 
    
    # Token para nueva línea
    'NEWLINE',

    # Palabras reservadas
    'RETURN', 'CONTINUE', 'BREAK', 'VAR',
    'IF', 'ELIF', 'ELSE', 'FOR', 'WHILE', 'FUN', 'MODEL', 'PRINT' , "COMMENT"
)

# Palabras clave
reserved = {
    'return': 'RETURN', # Palabra clave para retornar valores
    'continue': 'CONTINUE', # Palabra clave para continuar con la siguiente iteración
    'break': 'BREAK', # Palabra clave para salir de un ciclo
    'var': 'VAR', # Palabra clave para declarar variables
    'and': 'AND', # Palabra clave para el operador lógico AND
    'or': 'OR', # Palabra clave para el operador lógico OR
    'not': 'NOT', # Palabra clave para el operador lógico NOT
    'if': 'IF', # Palabra clave para la estructura condicional if
    'elif': 'ELIF', # Palabra clave para la estructura condicional else if
    'else': 'ELSE', # Palabra clave para la estructura condicional else
    'for': 'FOR', # Palabra clave para la estructura de repetición for
    'while': 'WHILE', # Palabra clave para la estructura de repetición while
    'fun': 'FUN', # Palabra clave para la declaración de funciones
    'model': 'MODEL', # Palabra clave para la declaración de modelos
    'print': 'PRINT' # Palabra clave para imprimir valores
}

# Definición de los patrones de los tokens

# Tipos de datos y valores
def t_NUMBER(t):
    r'[-+]?\d+(\.\d+)?([eE][-+]?\d+)?'
    t.value = float(t.value) if '.' in t.value or 'e' in t.value or 'E' in t.value else int(t.value)
    return t

def t_BOOL(t):
    r'\btrue\b|\bfalse\b'
    t.value = True if t.value == 'true' else False
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remover comillas
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Operadores lógicos
def t_AND(t):
    r'\band\b'
    return t

def t_OR(t):
    r'\bor\b'
    return t

def t_NOT(t):
    r'\bnot\b'
    return t

# Operadores aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_POW = r'\^'

# Operadores de comparación
t_EQ = r'='
t_NE = r'!='
t_EE = r'=='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='

# Símbolos y otros
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'  # Token para llave izquierda
t_RBRACE = r'\}'  # Token para llave derecha

# Tokens separados
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'  # Token para el operador de punto

# Token para nuevas líneas
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Comentarios
def t_COMMENT(t):
    r'//.*'
    pass

# Caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Creación del lexer
lexer = lex.lex()
