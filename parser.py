import yacc
from lexicalAnalyzer import tokens
from lexicalAnalyzer import lexer

# <----- GRAMMAR ----->
def p_Program(p):
    '''
    Program : Declaration Program
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
    VariableDeclaration : Variable SEMICOLON
    '''

def p_Variable(p):
    '''
    Variable : Type ID
             | ID ID
    '''
    
def p_Type(p):
    '''
    Type : INT
         | DOUBLE
         | BOOLEAN
         | STRING
         | Type LEFTBRACKET RIGHTBRACKET
         | ID LEFTBRACKET RIGHTBRACKET
    '''
    
def p_FunctionDeclaration(p):
    '''
    FunctionDeclaration : Type ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | Type ID LEFTPAREN RIGHTPAREN StatementBlock
                        | ID ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | ID ID LEFTPAREN RIGHTPAREN StatementBlock
                        | VOID ID LEFTPAREN Formals RIGHTPAREN StatementBlock
                        | VOID ID LEFTPAREN RIGHTPAREN StatementBlock
    '''
    
def p_Formals(p):
    '''
    Formals : Variable COMMA Formals
            | Variable
    '''
    
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
    
def p_IdList(p):
    '''
    IdList : ID COMMA IdList
           | ID
    '''
    
def p_Fields(p):
    '''
    Fields : Field Fields
           | Field
    '''
    
def p_Field(p):
    '''
    Field : VariableDeclaration
          | FunctionDeclaration
    '''
    
def p_InterfaceDeclaration(p):
    '''
    InterfaceDeclaration : INTERFACE ID LEFTBRACE Prototypes RIGHTBRACE
                         | INTERFACE ID LEFTBRACE RIGHTBRACE
    '''
    
def p_Prototypes(p):
    '''
    Prototypes : Prototype Prototypes
               | Prototype
    '''
    
def p_Prototype(p):
    '''
    Prototype : Type ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | Type ID LEFTPAREN RIGHTPAREN SEMICOLON
              | ID ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | ID ID LEFTPAREN RIGHTPAREN SEMICOLON
              | VOID ID LEFTPAREN Formals RIGHTPAREN SEMICOLON
              | VOID ID LEFTPAREN RIGHTPAREN SEMICOLON
    '''
    
def p_StatementBlock(p):
    '''
    StatementBlock : LEFTBRACE VaribleDeclarations Statements RIGHTBRACE
                   | LEFTBRACE Statements RIGHTBRACE
                   | LEFTBRACE VaribleDeclarations RIGHTBRACE
                   | LEFTBRACE RIGHTBRACE
    '''
    
def p_VaribleDeclarations(p):
    '''
    VaribleDeclarations : VariableDeclaration VaribleDeclarations
                        | VariableDeclaration
    '''
    
def p_Statements(p):
    '''
    Statements : Statement Statements
               | Statement 
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
    IfStatement : IF LEFTPAREN Expression RIGHTPAREN Statement ELSE Statement
                | IF LEFTPAREN Expression RIGHTPAREN Statement
    '''
    
def p_WhileStatement(p):
    '''
    WhileStatement : WHILE LEFTPAREN Expression RIGHTPAREN Statement
    '''
    
def p_ForStatement(p):
    '''
    ForStatement : FOR LEFTPAREN Expression SEMICOLON Expression SEMICOLON Expression RIGHTPAREN Statement
                 | FOR LEFTPAREN SEMICOLON Expression SEMICOLON Expression RIGHTPAREN Statement
                 | FOR LEFTPAREN Expression SEMICOLON Expression SEMICOLON RIGHTPAREN Statement
                 | FOR LEFTPAREN SEMICOLON Expression SEMICOLON RIGHTPAREN Statement
    '''
    
def p_BreakStatement(p):
    '''
    BreakStatement : BREAK SEMICOLON
    '''
    
def p_ReturnStatement(p):
    '''
    ReturnStatement : RETURN Expression SEMICOLON
                    | RETURN SEMICOLON
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
    
def p_UminusExpression(p):
    '''
    UminusExpression : MINUS Expression %prec UMINUS
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
    
def p_LValue(p):
    '''
    LValue : ID
         | LValue LEFTBRACKET Expression RIGHTBRACKET
         | LValue PERIOD ID
    '''
    
def p_Call(p):
    '''
    Call : ID LEFTPAREN Actuals RIGHTPAREN
         | ID LEFTPAREN RIGHTPAREN
         | ID PERIOD ID LEFTPAREN Actuals RIGHTPAREN
         | ID PERIOD ID LEFTPAREN RIGHTPAREN
    '''
    
def p_Actuals(p):
    '''
    Actuals : ExpressionList
    '''
    
def p_Constant(p):
    '''
    Constant : INTCONSTANT
             | DOUBLECONSTANT
             | STRINGCONSTANT
             | BOOLEANCONSTANT
             | NULL
    '''

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
input = "void f(double x, double y) { for ( ;x < 10 ; ) x = 1; }"
parser.parse(input,lexer)