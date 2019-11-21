'''
---------- START OF PROJECT 1 ----------
'''

import lex
import yacc

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

# read input from file, tokenize, and print
# file = open("toy_program.txt", "r")
# if file.mode == 'r':
#     lexer.input(file.read())
#     for tok in lexer:
#         print(tok)

'''
---------- END OF PROJECT 1 ----------
'''


'''
---------- START OF PROJECT 2 ----------
'''

# <----- GRAMMAR ----->
def p_Program(p):
    '''
    Program : Program Declaration
            | Declaration 
    '''
    
def p_Declaration(p):
    '''
    Declaration : VariableDeclaration
                | FunctionDeclaration
                | ClassDeclaration
                | InterfaceDeclaration
    '''
    
def p_VariableDeclaration(p):
    '''
    VariableDeclaration : Variable
    '''

def p_Variable(p):
    '''
    Variable : Type ID
    '''
    
def p_Type(p):
    '''
    Type : INT
         | DOUBLE
         | BOOLEAN
         | STRING
         | Type LEFTBRACKET RIGHTBRACKET
         | ID
    '''
    
def p_FunctionDeclaration(p):
    '''
    FunctionDeclaration : Type ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | VOID ID LEFTPAREN Formals RIGHTPAREN StatementBlock
    '''
    
def p_Formals(p):
    '''
    Formals : VariableList
            | empty
    '''
    
def p_VariableList(p):
    '''
    VariableList : Variable COMMA VariableList
                 | Variable
    '''
    
def p_ClassDeclaration(p):
    '''
    ClassDeclaration : CLASS ID ClassOptions LEFTBRACE FieldKleene RIGHTBRACE
    '''

def p_ClassOptions(p):
    '''
    ClassOptions : EXTENDS ID
                 | IMPLEMENTS IdList
                 | EXTENDS ID IMPLEMENTS IdList
                 | empty
    '''
    
def p_IdList(p):
    '''
    IdList : ID COMMA IdList
           | ID
    '''
    
def p_FieldKleene(p):
    '''
    FieldKleene : Field FieldKleene
                | empty
    '''
    
def p_Field(p):
    '''
    Field : VariableDeclaration
          | FunctionDeclaration
    '''
    
def p_InterfaceDeclaration(p):
    '''
    InterfaceDeclaration : INTERFACE ID LEFTBRACE PrototypeKleene RIGHTBRACE
    '''
    
def p_PrototypeKleene(p):
    '''
    PrototypeKleene : Prototype PrototypeKleene
                    | empty
    '''
    
def p_Prototype(p):
    '''
    Prototype : Type ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | VOID ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
    '''
    
def p_StatementBlock(p):
    '''
    StatementBlock : LEFTBRACE VaribleDeclarationKleene StatementKleene RIGHTBRACE
    '''
    
def p_VaribleDeclarationKleene(p):
    '''
    VaribleDeclarationKleene : VariableDeclaration VaribleDeclarationKleene
                             | empty
    '''
    
def p_StatementKleene(p):
    '''
    StatementKleene : Statement StatementKleene
                    | empty
    '''
    
def p_Statement(p):
    '''
    Statement : Expression SEMICOLON
              | SEMICOLON
              | IfStatement
              | WhileStatement
              | ForStatement
              | BreakStatement
              | ReturnStatement
              | PrintStatement
              | StatementBlock
    '''
    
def p_IfStatement(p):
    '''
    IfStatement : IF LEFTPAREN Expression RIGHTPAREN Statement OptionalElse
    '''
    
def p_OptionalElse(p):
    '''
    OptionalElse : ELSE Statement
                 | empty
    '''
    
def p_WhileStatement(p):
    '''
    WhileStatement : WHILE LEFTPAREN Expression RIGHTPAREN Statement
    '''
    
def p_ForStatement(p):
    '''
    ForStatement : FOR LEFTPAREN OptionalExpression SEMICOLON Expression SEMICOLON OptionalExpression RIGHTPAREN Statement
    '''
    
def p_OptionalExpression(p):
    '''
    OptionalExpression : Expression
                       | empty
    '''
    
def p_BreakStatement(p):
    '''
    BreakStatement : BREAK SEMICOLON
    '''
    
def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN OptionalExpression SEMICOLON
    '''
    
def p_PrintStatement(p):
    '''
    PrintStatement : PRINTLN LEFTPAREN ExpressionList RIGHTPAREN SEMICOLON
    '''
    
def p_ExpressionList(p):
    '''
    ExpressionList : Expression COMMA ExpressionList
                   | Expression
    '''
    
def p_Expression(p):
    '''
    Expression : LVal ASSIGNOP Expression
               | Constant
               | LVal
               | THIS
               | Call
               | LEFTPAREN Expression RIGHTPAREN
               | MINUS Expression
               | Expression ArithmaticOperator Expression
               | Expression CompareOperator Expression
               | Expression LogicalOperator Expression
               | NOT Expression
               | READLN LEFTPAREN RIGHTPAREN
               | NEW LEFTPAREN ID RIGHTPAREN
               | NEWARRAY LEFTPAREN INTCONSTANT COMMA Type RIGHTPAREN
    '''
    
def p_ArithmaticOperator(p):
    '''
    ArithmaticOperator : PLUS
                       | MINUS
                       | MULTIPLICATION
                       | DIVISION
                       | MOD
    '''
    
def p_CompareOperator(p):
    '''
    CompareOperator : LESS
                    | LESSEQUAL
                    | GREATER
                    | GREATEREQUAL
                    | EQUAL
                    | NOTEQUAL
    '''
    
def p_LogicalOperator(p):
    '''
    LogicalOperator : AND
                    | OR
    '''
    
def p_LVal(p):
    '''
    LVal : ID
         | LVal LEFTBRACKET Expression RIGHTBRACKET
         | LVal PERIOD ID
    '''
    
def p_Call(p):
    '''
    Call : ID LEFTPAREN Actuals RIGHTPAREN
         | ID PERIOD ID LEFTPAREN Actuals RIGHTPAREN
    '''
    
def p_Actual(p):
    '''
    Actuals : ExpressionList
            | empty
    '''
    
def p_Constant(p):
    '''
    Constant : INTCONSTANT
             | DOUBLECONSTANT
             | STRINGCONSTANT
             | BOOLEANCONSTANT
             | NULL
    '''
    
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    
   
# Build the parser
parser = yacc.yacc()


#parser.parse('',lexer)
    
'''
---------- END OF PROJECT 2 ----------
'''