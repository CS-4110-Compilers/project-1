

tokens = (
    'BOOLEAN', 'ELSE', 'IMPLEMENTS', 'NEWARRAY', 'RETURN', 'WHILE', 'DIVISION', 'GREATER', 'AND', 'SEMICOLON',
    'RIGHTPAREN', 'RIGHTBRACE', 'BOOLEANCONSTANT', 'BREAK', 'EXTENDS', 'INT', 'NULL', 'STRING', 'PLUS', 'MOD',
    'GREATEREQUAL', 'OR', 'COMMA', 'LEFTBRACKET', 'INTCONSTANT', 'ID', 'CLASS', 'FOR', 'INTERFACE', 'PRINTLN', 'THIS',
    'MINUS', 'LESS', 'EQUAL', 'NOT', 'PERIOD', 'RIGHTBRACKET', 'DOUBLECONSTANT', 'DOUBLE', 'IF', 'NEW', 'READLN',
    'VOID', 'MULTIPLICATION', 'LESSEQUAL', 'NOTEQUAL', 'ASSIGNOP', 'LEFTPAREN', 'LEFTBRACE', 'STRINGCONSTANT'
)

# tokens
t_DIVISION = r'\/'
t_GREATER = r'\>'
t_SEMICOLON = r'\;'
t_GREATEREQUAL = r'\>='
t_COMMA = r'\,'
t_LEFTBRACKET = r'\['
t_MINUS = r'\-'
t_LESS = r'\<'
t_EQUAL = r'\='
t_MULTIPLICATION = r'\*'
t_LESSEQUAL = r'\<='
t_NOTEQUAL = r'\!='
t_LEFTPAREN = r'\('
t_LEFTBRACE = r'\{'
t_RIGHTPAREN = r'\)'
t_RIGHTBRACE = r'\}'
t_PLUS = r'\+'
t_MOD = r'\%'
t_PERIOD = r'\.'
t_AND = r'\&&'
t_ELSE = r'\else'
t_NOT = r'\!'
t_RIGHTBRACKET = r'\]'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'


t_BOOLEANCONSTANT = ''
t_INTCONSTANT = ''
t_DOUBLECONSTANT = ''
t_NEW = ''
t_ASSIGNOP = ''
t_STRINGCONSTANT = ''

# reserved words
t_BOOLEAN = r'\boolean'
t_BREAK = r'\break'
t_READLN = r'\readln'
t_PRINTLN = r'\println'
t_IF = r'\if'
ELSE = r'\else'
CLASS = r'\class'
FOR = r'\for'
INTERFACE = r'\interface'
NULL = r'\null'
STRING = ''
RETURN = r'\return'
WHILE = r'\while'
THIS = r'\this'
IMPLEMENTS = r'\implements'
NEWARRAY = r'\newarray'
VOID = r'\void'
EXTENDS = r'\extends'

def t_DOUBLE(t):
    r'\d\.\d+'
    t.value = float(t)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

