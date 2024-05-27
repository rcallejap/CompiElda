import sys
from antlr4 import *
from little_duckLexer import little_duckLexer
from little_duckParser import little_duckParser
from little_duckVisitor import little_duckVisitor
from little_duckListener import little_duckListener
from MemorryManager import MemoryManager
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

    funcDir = listener.function_directory
    constDir = listener.ConstantTable 

    funcDir.test_print()
    print("const:") 
    constDir.test_print() 

    #memorry = MemoryManager(funcDir, constDir)
    #memoryArr = memorry.memory

    ##print(memoryArr)




if __name__ == '__main__':
    main(sys.argv)
