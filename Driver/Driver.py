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

    funcDir = listener.functionDirectory
    constDir = listener.ConstantTable 

    MemoryManager(funcDir, constDir)


    #entrega 3
    visitor = little_duckVisitor(funcDir, constDir)
    visitor.visit(tree)

    print ("Operator: ", visitor.operator_stack)
    print ("Operand: ", visitor.operand_stack)

    print("Quads: ")
    i = 0
    for Cuadroplo in visitor.quad_list:
        print(f"{i} ", end="")
        Cuadroplo.test_print()
        i += 1





if __name__ == '__main__':
    main(sys.argv)
