import sys
from antlr4 import *
from little_duckLexer import little_duckLexer
from little_duckParser import little_duckParser
from little_duckVisitor import little_duckVisitor
from little_duckListener import little_duckListener
from MemorryManager import MemoryManager
from virtualMachine import VirtualMachine
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
    visitor = little_duckVisitor(funcDir, constDir, MemorryCountArrayCopy)
    visitor.visit(tree)

    #Memorry Manager
    mManager.update(MemorryCountArrayCopy)
    memory = [[], mManager.memoryInt, mManager.memoryFloat, mManager.memoryBool, mManager.memoryString]
    quads= visitor.quad_list

    #Virtual Machine
    virtualMachine = VirtualMachine(quads, memory)
    virtualMachine.run()
    


    





if __name__ == '__main__':
    main(sys.argv)
