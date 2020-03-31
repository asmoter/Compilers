import sys

import ply.lex as lex

reserved = {
    'if': 'IF',
    # 'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

tokens = ['DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
          'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
          'LESSEQUAL', 'MOREEQUAL', 'NOTEQUAL', 'EQUAL',
          'ID', 'FLOAT', 'INTNUM', 'STRING', 'TRANSPOSE'] + list(reserved.values())

literals = ['+', '-', '*', '=', ':', ';', ',', '/', '>', '<', '(', ')', '[', ']', '{', '}']

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'\-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LESSEQUAL = r'<='
t_MOREEQUAL = r'>='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_TRANSPOSE = r'\''
t_ignore = '  \t'
t_ignore_COMMENT = r'\#.*'


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_FLOAT(t):
    r'([0-9]*\.[0-9]+([E][-]*[1-9])*|[0-9]+\.[0-9]*([E][-]*[1-9])*)'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'[1-9][0-9]*|0'
    t.value = int(t.value)
    return t


# def t_STRING(t):
#     r'("[a-zA-Z ]*")'
#     return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t


def t_newline(t):  # obsluga numerow linii
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("line %d: Illegal character '%s'" % (token.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
fh = open(sys.argv[1], "r")
lexer.input(fh.read())
for token in lexer:
    print("line %d: %s(%s)" % (token.lineno, token.type, token.value))

