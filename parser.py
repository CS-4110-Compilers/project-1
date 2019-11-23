import yacc
from lexicalAnalyzer import tokens
from lexicalAnalyzer import lexer
import logging
import pandas as pd


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

# function proess values
def clean_data(d_list: list) -> dict:
    data_dict = {
        'State': None,
        'Stack': None,
        'Action': None,
        'Result': None
    }
    acum = ''
    for element in d_list:
        for char in element:
            acum += char
            if acum in data_dict:
                key = acum
                element = element[element.index(':')+1:]
                element = element.rstrip('\n')
                data_dict[key] = element
        acum = ''

    # print(data_dict) # debug purposes
    return data_dict


if __name__ == '__main__':
    # craete logging object
    logging.basicConfig(
        level = logging.DEBUG,
        filename="debug_output.txt",
        filemode = 'w',
        format = '%(filename)10s:%(lineno)4d:%(message)s'
    )
    log = logging.getLogger()
    # args for yacc debug=True,debuglog=log when debugging
    # Build the parser
    parser = yacc.yacc(debug=True,debuglog=log)

    input_string = "void f(double x, double y) { for ( ;x < 10 ; ) x = 1; }"

    # when gnerating log file change debug to log
    debug_info = parser.parse(input_string, lexer, debug=log)

    # # create file to store debug output for future/further processing
    # with open('debug_data.txt','w',encoding='utf-8') as f:
    #     f.write(debug_info)

    # ---------- beginning of output processing ------------------ #
    buffer = []
    t_data = []
    tmp_group = []
    data_list = []
    b_string = 'PARSE DEBUG START'  # beginning line
    e_string = 'PARSE DEBUG END'    # ending line of debug
    d_string = 'Done'  # last line of log file

    # Create dataframe
    df = pd.DataFrame(columns=['State','Stack','Action','Result'])


    with open('debug_output.txt', encoding='utf-8') as f:
        for line in f:
            if line != '\n':
                if b_string not in line and e_string not in line and d_string not in line:
                    line = line.replace('yacc.py:', '')
                    line =line[line.index(':')+1:]
                    buffer.append(line)

    for line in buffer:
        if len(line) == 1:
            tmp_dict = clean_data(tmp_group)
            data_list.append(tmp_dict)
            df = df.append(tmp_dict,ignore_index=True)
            tmp_group = []
        else:
            tmp_group.append(line)
    # drop first row as it only contians Null values
    df = df.drop(index=0)

    # reset index
    df = df.reset_index()

    # kick off indexing to being at 1
    df = df.shift()[1:]

    # export dataframe to excel spread sheet
    # NOTE requries openpyxl (??) package if using pychamr easily search and install
    # via pycharm project prefs

    # for csv file uncomment line below
    # df.to_csv('shift_reduce_trace.csv')
    df.to_excel('shift_reduce_trace.xlsx')

    # note to_excel & to_csv will create correspodning file in directory as program is running
    # please send coffee
    # ------------ End of Data Processing ------------- #
>>>>>>> ab1608cd26fbe5b725ed7582d0c16c0c2e97e812
