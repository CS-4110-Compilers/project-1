import yacc
from lexicalAnalyzer import tokens
from lexicalAnalyzer import lexer

# <----- GRAMMAR ----->
def p_Program(p):
    '''
    Program : Declaration Program
            | Declaration 
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+" "+p[2]
    
def p_Declaration(p):
    '''
    Declaration : VariableDeclaration
                | FunctionDeclaration
                | ClassDeclaration
                | InterfaceDeclaration
    '''
    p[0] = p[1]
    
def p_VariableDeclaration(p):
    '''
    VariableDeclaration : Variable SEMICOLON
    '''
    p[0] = p[1]+" "+p[2]
    
def p_Variable(p):
    '''
    Variable : Type ID
             | ID ID
    '''
    p[0] = p[1]+" "+p[2]
    
def p_Type(p):
    '''
    Type : INT
         | DOUBLE
         | BOOLEAN
         | STRING
         | Type LEFTBRACKET RIGHTBRACKET
         | ID LEFTBRACKET RIGHTBRACKET
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    
def p_FunctionDeclaration(p):
    '''
    FunctionDeclaration : Type ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | Type ID LEFTPAREN RIGHTPAREN StatementBlock
                        | ID ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | ID ID LEFTPAREN RIGHTPAREN StatementBlock
                        | VOID ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | VOID ID LEFTPAREN RIGHTPAREN StatementBlock
    '''
    if len(p) == 7:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]
    elif len(p) == 6:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    
def p_Formals(p):
    '''
    Formals : Variable COMMA Formals
            | Variable
    '''
    if len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]
    
def p_ClassDeclaration(p):
    '''
    ClassDeclaration : CLASS ID EXTENDS ID LEFTBRACE Fields RIGHTBRACE
                     | CLASS ID IMPLEMENTS IdList LEFTBRACE Fields RIGHTBRACE
                     | CLASS ID EXTENDS ID IMPLEMENTS IdList LEFTBRACE Fields RIGHTBRACE
                     | CLASS ID LEFTBRACE Fields RIGHTBRACE
                     | CLASS ID EXTENDS ID LEFTBRACE RIGHTBRACE
                     | CLASS ID IMPLEMENTS IdList LEFTBRACE RIGHTBRACE
                     | CLASS ID EXTENDS ID IMPLEMENTS IdList LEFTBRACE RIGHTBRACE
                     | CLASS ID LEFTBRACE RIGHTBRACE
    '''
    if len(p) == 10:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]+" "+p[8]+" "+p[9]
    elif len(p) == 9:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]+" "+p[8]    
    elif len(p) == 8:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]
    elif len(p) == 7:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]
    elif len(p) == 6:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    else:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]
    
def p_IdList(p):
    '''
    IdList : ID COMMA IdList
           | ID
    '''
    if len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]
    
def p_Fields(p):
    '''
    Fields : Field Fields
           | Field
    '''
    if len(p) == 3:
        p[0] = p[1]+" "+p[2]
    else:
        p[0] = p[1]
    
def p_Field(p):
    '''
    Field : VariableDeclaration
          | FunctionDeclaration
    '''
    p[0] = p[1]
    
def p_InterfaceDeclaration(p):
    '''
    InterfaceDeclaration : INTERFACE ID LEFTBRACE Prototypes RIGHTBRACE
                         | INTERFACE ID LEFTBRACE RIGHTBRACE
    '''
    if len(p) == 6:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    else:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]
    
def p_Prototypes(p):
    '''
    Prototypes : Prototype Prototypes
               | Prototype
    '''
    if len(p) == 3:
        p[0] = p[1]+" "+p[2]
    else:
        p[0] = p[1]
    
def p_Prototype(p):
    '''
    Prototype : Type ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | Type ID LEFTPAREN RIGHTPAREN SEMICOLON
              | ID ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | ID ID LEFTPAREN RIGHTPAREN SEMICOLON
              | VOID ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | VOID ID LEFTPAREN RIGHTPAREN SEMICOLON
    '''
    if len(p) == 7:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]
    else:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    
def p_StatementBlock(p):
    '''
    StatementBlock : LEFTBRACE VaribleDeclarations Statements RIGHTBRACE
                   | LEFTBRACE Statements RIGHTBRACE
                   | LEFTBRACE VaribleDeclarations RIGHTBRACE
                   | LEFTBRACE RIGHTBRACE
    '''
    if len(p) == 5:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]
    elif len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]+" "+p[2]
    
def p_VaribleDeclarations(p):
    '''
    VaribleDeclarations : VariableDeclaration VaribleDeclarations
                        | VariableDeclaration
    '''
    if len(p) == 3:
        p[0] = p[1]+" "+p[2]
    else:
        p[0] = p[1]
    
def p_Statements(p):
    '''
    Statements : Statement Statements
               | Statement 
    '''
    if len(p) == 3:
        p[0] = p[1]+" "+p[2]
    else:
        p[0] = p[1]
    
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
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+" "+p[2]
    
def p_IfStatement(p):
    '''
    IfStatement : IF LEFTPAREN Expression RIGHTPAREN Statement ELSE Statement
                | IF LEFTPAREN Expression RIGHTPAREN Statement
    '''
    if len(p) == 8:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]   
    else:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    
def p_WhileStatement(p):
    '''
    WhileStatement : WHILE LEFTPAREN Expression RIGHTPAREN Statement
    '''
    p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    
def p_ForStatement(p):
    '''
    ForStatement : FOR LEFTPAREN Expression SEMICOLON Expression SEMICOLON Expression RIGHTPAREN Statement
                 | FOR LEFTPAREN SEMICOLON Expression SEMICOLON Expression RIGHTPAREN Statement
                 | FOR LEFTPAREN Expression SEMICOLON Expression SEMICOLON RIGHTPAREN Statement
                 | FOR LEFTPAREN SEMICOLON Expression SEMICOLON RIGHTPAREN Statement
    '''
    if len(p) == 10:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]+" "+p[8]+" "+p[9]
    elif len(p) == 9:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]+" "+p[8]    
    elif len(p) == 8:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]+" "+p[7]
    
def p_BreakStatement(p):
    '''
    BreakStatement : BREAK SEMICOLON
    '''
    p[0] = p[1]+" "+p[2]
    
def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN Expression SEMICOLON
                    | RETURN SEMICOLON
    '''
    if len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]+" "+p[2]
    
def p_PrintStatement(p):
    '''
    PrintStatement : PRINTLN LEFTPAREN ExpressionList RIGHTPAREN SEMICOLON
    '''
    p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]
    
def p_ExpressionList(p):
    '''
    ExpressionList : Expression COMMA ExpressionList
                   | Expression
    '''
    if len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]
    
def p_Expression(p):
    '''
    Expression : LValue ASSIGNOP Expression
               | Constant
               | LValue
               | THIS
               | Call
               | LEFTPAREN Expression RIGHTPAREN
               | UminusExpression
               | Expression ArithmaticOperator Expression
               | Expression CompareOperator Expression
               | Expression LogicalOperator Expression
               | NOT Expression
               | READLN LEFTPAREN RIGHTPAREN
               | NEW LEFTPAREN ID RIGHTPAREN
               | NEWARRAY LEFTPAREN INTCONSTANT COMMA Type RIGHTPAREN
               | NEWARRAY LEFTPAREN INTCONSTANT COMMA ID RIGHTPAREN
    '''
    if len(p) == 7:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]
    elif len(p) == 5:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]    
    elif len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    elif len(p) == 3:
        p[0] = p[1]+" "+p[2]
    else:
        p[0] = p[1]
    
def p_UminusExpression(p):
    '''
    UminusExpression : MINUS Expression %prec UMINUS
    '''
    p[0] = p[1]+" "+p[2]

def p_ArithmaticOperator(p):
    '''
    ArithmaticOperator : PLUS
                       | MINUS
                       | MULTIPLICATION
                       | DIVISION
                       | MOD
    '''
    p[0] = p[1]
    
def p_CompareOperator(p):
    '''
    CompareOperator : LESS
                    | LESSEQUAL
                    | GREATER
                    | GREATEREQUAL
                    | EQUAL
                    | NOTEQUAL
    '''
    p[0] = p[1]
    
def p_LogicalOperator(p):
    '''
    LogicalOperator : AND
                    | OR
    '''
    p[0] = p[1]
    
def p_LValue(p):
    '''
    LValue : ID
           | LValue LEFTBRACKET Expression RIGHTBRACKET
           | LValue PERIOD ID
    '''
    if len(p) == 5:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]
    elif len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    else:
        p[0] = p[1]
    
def p_Call(p):
    '''
    Call : ID LEFTPAREN Actuals RIGHTPAREN
         | ID LEFTPAREN RIGHTPAREN
         | ID PERIOD ID LEFTPAREN Actuals RIGHTPAREN
         | ID PERIOD ID LEFTPAREN RIGHTPAREN
    '''
    if len(p) == 7:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]+" "+p[6]
    elif len(p) == 6:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]+" "+p[5]  
    elif len(p) == 5:
        p[0] = p[1]+" "+p[2]+" "+p[3]+" "+p[4]
    elif len(p) == 4:
        p[0] = p[1]+" "+p[2]+" "+p[3]
    
def p_Actuals(p):
    '''
    Actuals : ExpressionList
    '''
    p[0] = p[1]
    
def p_Constant(p):
    '''
    Constant : INTCONSTANT
             | DOUBLECONSTANT
             | STRINGCONSTANT
             | BOOLEANCONSTANT
             | NULL
    '''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    
precedence = (
    ('nonassoc', 'ASSIGNOP'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUAL', 'NOTEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION', 'MOD'),
    ('right', 'NOT', 'UMINUS'),
    ('right', 'LEFTBRACKET', 'PERIOD')
)

# Build the parser
parser = yacc.yacc()

#read input from file, tokenize, and print
with open('toy_program.txt', 'r') as file:
    data = file.read().replace('\n', '')
    parser.parse(data,lexer, debug=True)
input = "class One { int oneInt; double f() { this.oneInt=3; } }"
print(data)
parser.parse(data,lexer, debug=True)