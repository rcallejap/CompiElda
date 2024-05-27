# recibe funcDir y agrega direccion de memoria a las variables

# Generated from little_duck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

from data_structures import Variable, VarTable, Function, FunctionDirectory, Cuadroplo
from cubo_semantico import check_cubo_semantico


class MemoryManager:
    def __init__(self, funcDir, constDir) : 
        self.funcDir = funcDir
        self.memoryInt = []
        self.memoryFloat = []
        self.memoryBool = []
        self.memoryString = []
        # make the memory array 10000 sizees and full of None
        
        self.intCount = 0
        self.floatCount = 0
        self.boolCount = 0
        self.stringCount = 0

        VarTable = funcDir.global_var_table
        
        VarTable.print_table()

        for var in VarTable.variables:
            if VarTable.variables[var].type == "int":
                self.memoryInt.append(None)
                varDir = 1000 + self.intCount
                VarTable.variables[var].dir = varDir
                self.intCount += 1
            elif VarTable.variables[var].type == "float":
                self.memoryFloat.append(None)
                varDir = 2000 + self.floatCount
                VarTable.variables[var].dir = varDir
                self.floatCount += 1
            elif VarTable.variables[var].type == "bool":
                self.memoryBool.append(None)
                varDir = 3000 + self.boolCount
                VarTable.variables[var].dir = varDir
                self.boolCount += 1
            elif VarTable.variables[var].type == "string":
                self.memoryString.append(None)
                varDir = 4000 + self.stringCount
                VarTable.variables[var].dir = varDir
                self.stringCount += 1
            
 

        for const in constDir.constants:
            if constDir.constants[const].type == "int":
                self.memoryInt.append(constDir.constants[const].value)
                constDir.constants[const].dir = 1000 + self.intCount
                self.intCount += 1
            elif constDir.constants[const].type == "float":
                self.memoryFloat.append(constDir.constants[const].value)
                constDir.constants[const].dir = 2000 + self.floatCount
                self.floatCount += 1
            elif constDir.constants[const].type == "bool":
                self.memoryBool.append(constDir.constants[const].value)
                constDir.constants[const].dir = 3000 + self.boolCount
                self.boolCount += 1
            elif constDir.constants[const].type == "string":
                self.memoryString.append(constDir.constants[const].value)
                constDir.constants[const].dir = 4000 + self.stringCount
                self.stringCount += 1