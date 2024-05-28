import sys
from antlr4 import *
from little_duckLexer import little_duckLexer
from little_duckParser import little_duckParser
from little_duckVisitorTester import little_duckVisitorTester
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

    mManager = MemoryManager(funcDir, constDir)

    MemorryCountArray = [mManager.intCount, mManager.floatCount, mManager.boolCount, mManager.stringCount]
    MemorryCountArrayCopy = MemorryCountArray.copy()

    #entrega 3
    visitor = little_duckVisitorTester(funcDir, constDir, MemorryCountArrayCopy)
    visitor.visit(tree)

    print ("Operator: ", visitor.operator_stack)
    print ("Operand: ", visitor.operand_stack)

    print("Quads: ")
    i = 0
    for Cuadroplo in visitor.quad_list:
        print(f"{i} ", end="")
        Cuadroplo.test_print()
        i += 1
    
    print (MemorryCountArray)
    print (MemorryCountArrayCopy)

    mManager.update(MemorryCountArrayCopy)






if __name__ == '__main__':
    main(sys.argv)
