import sys
from antlr4 import *
from little_duckLexer import little_duckLexer
from little_duckParser import little_duckParser
'''from VisitorInterp import VisitorInterp'''

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = little_duckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = little_duckParser(stream)
    tree = parser.start_()

if __name__ == '__main__':
    main(sys.argv)
