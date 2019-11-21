import yacc
from lexicalAnalyzer import tokens
from lexicalAnalyzer import lexer

# <----- GRAMMAR ----->
def p_Program(p):
    '''
    Program : Program Declaration
            | Declaration 
    '''
    if len(p) == 2:
        p[0] = '(Program:'+p[1]+')'
    else:
        p[0] = '(Program:'+p[1]+', '+'Declaration:'+p[2]+')'
    print(p[0])
    
def p_Declaration(p):
    '''
    Declaration : VariableDeclaration
                | FunctionDeclaration
                | ClassDeclaration
                | InterfaceDeclaration
    '''
    p[0] = '(Declaration:'+p[1]+')'
    
def p_VariableDeclaration(p):
    '''
    VariableDeclaration : Variable SEMICOLON
    '''
    p[0] = '(Variable:'+p[1]+', '+p[2]+')'

def p_Variable(p):
    '''
    Variable : Type ID
    '''
    p[0] = '(Type:'+p[1]+', ID:'+p[2]+')'
    
def p_Type(p):
    '''
    Type : INT
         | DOUBLE
         | BOOLEAN
         | STRING
         | Type LEFTBRACKET RIGHTBRACKET
         | ID
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]+p[2]+p[3]
    
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
               | UminusExpression
               | Expression ArithmaticOperator Expression
               | Expression CompareOperator Expression
               | Expression LogicalOperator Expression
               | NOT Expression
               | READLN LEFTPAREN RIGHTPAREN
               | NEW LEFTPAREN ID RIGHTPAREN
               | NEWARRAY LEFTPAREN INTCONSTANT COMMA Type RIGHTPAREN
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
    '''
    empty :
    '''
    pass

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
    ('nonassoc', 'LEFTBRACKET', 'PERIOD')
)

# Build the parser
parser = yacc.yacc()
parser.parse('int [] x;',lexer)