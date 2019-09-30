import ply.lex as lex
import ply.yacc as yacc
import sys

# reserved word list
reserved = {
    'boolean': 'BOOLEAN',
    'break': 'BREAK',
    'readln': 'READLN',
    'println': 'PRINTLN',
    'if': 'IF',
    'else': 'ELSE',
    'class': 'CLASS',
    'for': 'FOR',
    'interface': 'INTERFACE',
    'null': 'NULL',
    'string': 'STRING',
    'return': 'RETURN',
    'while': 'WHILE',
    'this': 'THIS',
    'implements': 'IMPLEMENTS',
    'newarray': 'NEWARRAY',
    'void': 'VOID',
    'extends': 'EXTENDS'
}

tokens = [
    'BOOLEAN', 'ELSE', 'IMPLEMENTS', 'NEWARRAY', 'RETURN', 'WHILE', 'DIVISION', 'GREATER', 'AND', 'SEMICOLON',
    'RIGHTPAREN', 'RIGHTBRACE', 'BOOLEANCONSTANT', 'BREAK', 'EXTENDS', 'INT', 'NULL', 'STRING', 'PLUS', 'MOD',
    'GREATEREQUAL', 'OR', 'COMMA', 'LEFTBRACKET', 'INTCONSTANT', 'ID', 'CLASS', 'FOR', 'INTERFACE', 'PRINTLN', 'THIS',
    'MINUS', 'LESS', 'EQUAL', 'NOT', 'PERIOD', 'RIGHTBRACKET', 'DOUBLECONSTANT', 'DOUBLE', 'IF', 'NEW', 'READLN',
    'VOID', 'MULTIPLICATION', 'LESSEQUAL', 'NOTEQUAL', 'ASSIGNOP', 'LEFTPAREN', 'LEFTBRACE', 'STRINGCONSTANT'
]

# token declarations
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
t_NOT = r'\!'
t_RIGHTBRACKET = r'\]'

# declaration to ignore white space
t_ignore = ' \t'

# t_BOOLEANCONSTANT = ''
# t_INTCONSTANT = ''
# t_DOUBLECONSTANT = ''
# t_NEW = ''
# t_ASSIGNOP = ''
# t_STRINGCONSTANT = ''

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

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


lexer = lex.lex()
lexer.input('if { print' )
while True:
    tok = lexer.token()
    if not tok:
        break
    else:
        print(tok)
