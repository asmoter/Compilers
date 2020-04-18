
import sys
import ply.yacc as yacc
from parser import parser
from TreePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = parser()
    parser = yacc.yacc(module=parser)
    text = file.read()
    ast = parser.parse(text, lexer=parser.scanner)
    ast.printTree()