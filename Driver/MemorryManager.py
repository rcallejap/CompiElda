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
    def __init__(self, function_directory, constDir) : 
        self.function_directory = function_directory
        self.memory = []
        # make the memory array 10000 sizees and full of None
        self.memoryCount = {
            "int": {
                "global": 1000,
                "const": 1300,
                "temp": 1600,
                "local": 1900
            },
            "float": {
                "global": 2000,
                "local": 2300,
                "temp": 2600,
                "local":2900

            },
            "bool" : {
                "global": 3000,
                "local": 3300,
                "temp": 3600,
                "local": 3900 
            },
            "string" : {
                "global": 4000,
                "local": 4300,
                "temp": 4600, 
                "local": 4900
            }
        }


        for var in function_directory.global_var_table.variables.values():
            self.add_variable(var, "global")
        
        
        for function in function_directory.functions.values():
            self.add_function(function)



    def add_variable(self, variable, scope): 
        memory = self.get_memory(variable.type, scope)
        print (variable.name, " ",  memory)

        #variable.dir = memory
        #self.memory[memory] = variable
        self.memoryCount[scope][variable.type] += 1   



    def get_memory(self, var_type, scope):
        if scope == "global":
            return self.memory["global"][var_type]
        elif scope == "local":
            return self.memory["local"][var_type]
        elif scope == "temp":
            return self.memory["temp"][var_type]
        else:
            raise Exception(f"Scope '{scope}' not recognized")
        

    def add_function(self, function):
        for var in function.var_table.variables.values():
            self.add_variable(var, "local")
        self.function_directory.add_function(function)