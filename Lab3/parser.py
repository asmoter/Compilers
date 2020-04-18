#!/usr/bin/python

import scanner
import ply.yacc as yacc

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


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


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


def p_block(p):
    """ block : '{' instructions '}' """


def p_if(p):
    """ if : IF '(' assignment ')' instruction %prec IFX
           | IF '(' assignment ')' instruction ELSE instruction """


def p_print(p):
    """ print : PRINT arguments ';' """


def p_arguments(p):
    """ arguments : assignment
                  | assignment ',' arguments """


def p_while(p):
    """ while : WHILE '(' assignment ')' instruction """


def p_for(p):
    """ for : FOR ID '=' range instruction """


def p_range(p):
    """ range : expression ':' expression """


def p_break(p):
    """ break : BREAK ';' """


def p_continue(p):
    """ continue : CONTINUE ';' """


def p_return(p):
    """ return : RETURN ';'
               | RETURN assignment ';' """


def p_assign(p):
    """ assign : ID '=' assign
               | ID '=' assignment ';'
               | ID ADDASSIGN assignment ';'
               | ID SUBASSIGN assignment ';'
               | ID MULASSIGN assignment ';'
               | ID DIVASSIGN assignment ';' """


def p_assign_in_array(p):
    """ assign_in_array : ID array_range '=' assign
                        | ID array_range '=' assignment ';'
                        | ID array_range ADDASSIGN assignment ';'
                        | ID array_range SUBASSIGN assignment ';'
                        | ID array_range MULASSIGN assignment ';'
                        | ID array_range DIVASSIGN assignment ';' """


def p_array_range(p):
    """ array_range : '[' INTNUM ',' INTNUM ']'
                    | '[' INTNUM ']' """


def p_assignment(p):
    """ assignment : STRING
                   | matrix_initialization
                   | relational_expression
                   | expression
                   | array """


def p_array(p):
    """ array : '[' ']'
              | '[' dimensions ']' """


def p_dimensions(p):
    """ dimensions : values
                   | values ';' dimensions """


def p_values(p):
    """ values : value
               | value ',' values """


def p_value(p):
    """ value : STRING
              | number """


def p_relational_expression(p):
    """ relational_expression : expression '<' expression
                              | expression '>' expression
                              | expression LESSEQUAL expression
                              | expression MOREEQUAL expression
                              | expression EQUAL expression
                              | expression NOTEQUAL expression """


def p_expression_binary_operation(p):
    """ expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression
                   | expression DOTADD expression
                   | expression DOTSUB expression
                   | expression DOTMUL expression
                   | expression DOTDIV expression """


def p_expression(p):
    """ expression : number
                   | ID """


def p_expression_transpose(p):
    """ expression : ID TRANSPOSE """


def p_expression_unegation(p):
    """ expression : '-' expression %prec UNEGATION """


def p_matrix_initialization(p):
    """ matrix_initialization : EYE '(' INTNUM ')'
                                | ZEROS '(' INTNUM ')'
                                | ONES '(' INTNUM ')' """


def p_number(p):
    """ number : INTNUM
               | FLOAT """


parser = yacc.yacc()
