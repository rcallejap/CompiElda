import sys
from antlr4 import *
from little_duckLexer import little_duckLexer
from little_duckParser import little_duckParser
'''from VisitorInterp import VisitorInterp'''
from little_duckListener import little_duckListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = little_duckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = little_duckParser(stream)
    tree = parser.start_()
    
    #entrega 2
    listener = little_duckListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
