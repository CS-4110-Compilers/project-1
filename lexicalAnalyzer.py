import lex

# <----- TOKENS ----->

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
    'extends': 'EXTENDS',
    'new': 'NEW',
    'double': 'DOUBLE',
    'int': 'INT',
    'false' : 'BOOLEANCONSTANT',
    'true' : 'BOOLEANCONSTANT'
}

# list of token names
tokens = [
        'DOUBLECONSTANT', 'INTCONSTANT', 'DIVISION', 'GREATER', 'AND', 'SEMICOLON', 'RIGHTPAREN', 'RIGHTBRACE',
        'PLUS', 'MOD', 'GREATEREQUAL', 'OR', 'COMMA', 'LEFTBRACKET',
        'ID', 'MINUS', 'LESS', 'EQUAL', 'NOT', 'PERIOD', 'RIGHTBRACKET',
        'MULTIPLICATION', 'LESSEQUAL', 'NOTEQUAL', 'ASSIGNOP',
        'LEFTPAREN', 'LEFTBRACE', 'STRINGCONSTANT'
    ] + list(reserved.values())

# operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_MOD = r'\%'
t_LESS = r'\<'
t_LESSEQUAL = r'\<='
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>='
t_EQUAL = r'\=='
t_NOTEQUAL = r'\!='
t_AND = r'\&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_ASSIGNOP = r'\='
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_PERIOD = r'\.'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'

# int constants
t_INTCONSTANT = r'0[xX][0-9a-fA-F]+|[0-9]+(?!\.)'

# double constants
t_DOUBLECONSTANT = r'[0-9]+\.[0-9]*([eE]([+-])?[0-9]+)?'

# string constants
t_STRINGCONSTANT = r'\"[^\"\n]*\"'

# identifiers
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# ignore comments
t_ignore_COMMENT = r'\/\/[^\n]*'
t_ignore_BLOCK_COMMENT = r'\/\*(.|\n)*\*\/'

# ignore white space
t_ignore_NEWLINE = r'\n'
t_ignore_SPACE = r'\s'
t_ignore_TAB = r'\t'

# illegal character handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# build the lexer
lexer = lex.lex()

#read input from file, tokenize, and print
# file = open("toy_program.txt", "r")
# if file.mode == 'r':
#     lexer.input(file.read())
#     for tok in lexer:
#         print(tok)