#!/usr/bin/python

import scanner
import ply.yacc as yacc
import AST

tokens = scanner.tokens

precedence = (
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),
    ("nonassoc", "=", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
    ("nonassoc", "EQUAL", "NOTEQUAL"),
    ("nonassoc", "<", ">", "LESSEQUAL", "MOREEQUAL"),
    ("left", '+', '-', "DOTADD", "DOTSUB"),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
    ("right", "UNEGATION"),
    ("left", "TRANSPOSE")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno,  p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = p[1]


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = p[1]


def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = AST.OperationNode()


def p_instructions_1(p):
    """instructions : instructions instruction """
    p[0] = p[1]
    p[0].append(p[2])


def p_instructions_2(p):
    """instructions : instruction """
    p[0] = p[1]


def p_instruction(p):
    """instruction : block
                   | if
                   | print
                   | while
                   | for
                   | break
                   | continue
                   | return
                   | assign
                   | assign_in_array """
    p[0] = p[1]


def p_block(p):
    """ block : '{' instructions '}' """
    p[0] = p[1]


def p_if(p):
    """ if : IF '(' assignment ')' instruction %prec IFX"""
    p[0] = AST.IfExpr(p[3], p[5])


def p_if_else(p):
    """ if : IF '(' assignment ')' instruction ELSE instruction """
    p[0] = AST.IfElseExpr(p[3], p[5], p[7])


def p_print(p):
    """ print : PRINT arguments ';' """
    p[0] = AST.Print(p[2])


def p_arguments(p):
    """ arguments : assignment
                  | assignment ',' arguments """
    p[0] = AST.Arguments(p[1])


def p_while(p):
    """ while : WHILE '(' assignment ')' instruction """
    p[0] = AST.WhileLoop(p[3], p[5])


def p_for(p):
    """ for : FOR ID '=' range instruction """
    p[0] = AST.ForLoop(p[1], p[3], p[5])


def p_range(p):
    """ range : expression ':' expression """
    p[0] = AST.Range(p[1], p[3])


def p_break(p):
    """ break : BREAK ';' """
    p[0] = AST.Break()


def p_continue(p):
    """ continue : CONTINUE ';' """
    p[0] = AST.Continue();


def p_return(p):
    """ return : RETURN ';' """
    p[0] = AST.Return()


def p_returnValue(p):
    """ return : RETURN assignment ';' """
    p[0] = AST.ReturnValue(p[2])


def p_assign(p):
    """ assign : ID '=' assign
               | ID '=' assignment ';'
               | ID ADDASSIGN assignment ';'
               | ID SUBASSIGN assignment ';'
               | ID MULASSIGN assignment ';'
               | ID DIVASSIGN assignment ';' """
    p[0] = AST.AssignExpr(p[2], p[1], p[3])


def p_assign_in_array(p):
    """ assign_in_array : ID array_range '=' assign
                        | ID array_range '=' assignment ';'
                        | ID array_range ADDASSIGN assignment ';'
                        | ID array_range SUBASSIGN assignment ';'
                        | ID array_range MULASSIGN assignment ';'
                        | ID array_range DIVASSIGN assignment ';' """
    p[0] = AST.AssignInArrayExpr(p[3], p[1], p[2], p[4])


def p_array_range(p):
    """ array_range : '[' INTNUM ',' INTNUM ']'
                    | '[' INTNUM ']' """


def p_assignment(p):
    """ assignment : STRING
                   | matrix_initialization
                   | relational_expression
                   | expression
                   | array """
    p[0] = p[1]


def p_array(p):
    """ array : '[' ']' """
    p[0] = AST.Array()


def p_array2(p):
    """ array : '[' dimensions ']' """
    p[0] = AST.Array(p[1])


def p_dimensions(p):
    """ dimensions : values """
                   # | values ';' dimensions """
    # p[0] = AST.Dimensions(p[1], p[3])
    p[0] = AST.Dimensions(p[1])


def p_values(p):
    """ values : value """
    p[0] = p[1]


def p_values2(p):
    """ values : value ',' values """
    p[0] = p[1]
    p[0].append(p[3])


def p_value(p):
    """ value : STRING
              | number """
    p[0] = p[1]


def p_relational_expression(p):
    """ relational_expression : expression '<' expression
                              | expression '>' expression
                              | expression LESSEQUAL expression
                              | expression MOREEQUAL expression
                              | expression EQUAL expression
                              | expression NOTEQUAL expression """
    p[0] = AST.RelExpr(p[2], p[1], p[3])


def p_expression_binary_operation(p):
    """ expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression
                   | expression DOTADD expression
                   | expression DOTSUB expression
                   | expression DOTMUL expression
                   | expression DOTDIV expression """
    p[0] = AST.BinExpr(p[2], p[1], p[3])


def p_expression(p):
    """ expression : number
                   | ID """
    p[0] = p[1]


def p_expression_transpose(p):
    """ expression : ID TRANSPOSE """
    p[0] = AST.Transposition(p[1])


def p_expression_unegation(p):
    """ expression : '-' expression %prec UNEGATION """
    p[0] = AST.UNegation(p[2])


def p_matrix_initialization(p):
    """ matrix_initialization : EYE '(' INTNUM ')'
                                | ZEROS '(' INTNUM ')'
                                | ONES '(' INTNUM ')' """
    p[0] = AST.MatrixInitialization(p[1], p[2])


def p_number(p):
    """ number : INTNUM
               | FLOAT """
    p[0] = p[1]


parser = yacc.yacc()
