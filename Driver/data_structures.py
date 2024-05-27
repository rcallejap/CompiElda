# Estrucutras de datos de cuadruplo
class Cuadroplo:
    def __init__ (self, op, left, right, result, scope):
        self.op = op
        self.left = left
        self.right = right
        self.result = result
        self.scope = scope

    def test_print(self): 
        print(f" {self.op} {self.left} {self.right} {self.result} ({self.scope}) ")
    

## Estructuras de datos de la tabla de funciones
class Variable:
    def __init__(self, name, vtype):
        self.name = name 
        self.type = vtype
        self.dir = None

class VarTable:
    def __init__(self):
        self.variables = {} #diccionario de variables

class Function:
    def __init__(self,name ):
        self.name = name
        self.var_table = VarTable() #tabla de variables de la funcion

class FunctionDirectory:
    def __init__(self):
        self.functions = {}
        #add a global var table
        self.global_var_table = VarTable()


    def add_function(self, functionN):
        if functionN in self.functions:
            raise Exception(f"Function '{function.name}' already declared")
        self.functions[functionN] = Function(functionN) 


    def add_variable(self, variable, function_name):
        #if the function name does not exist raise an exception
        if function_name != "global" and function_name not in self.functions:
            raise Exception(f"Function '{function_name}' not declared")

        if variable.name in self.global_var_table.variables:
            raise Exception(f"Variable '{variable.name}' already declared")        
        
        if function_name == "global":
            self.global_var_table.variables[variable.name] = variable
        
        else:
            if variable.name in self.functions[function_name].var_table.variables:
                raise Exception(f"Variable '{variable.name}' already declared")
            
            if function_name not in self.functions:
                raise Exception(f"Function '{function_name}' not declared")
            
            self.functions[function_name].var_table.variables[variable.name] = variable

    def test_print(self):
        print("Global var table")
        for var in self.global_var_table.variables.values():
            print(f"{var.name} : {var.type} = {var.dir}")

        print("_Functions:")
        for function in self.functions.values():
            print(f"    Function {function.name}")
            for var in function.var_table.variables.values():
                print(f"        {var.name} : {var.type} = {var.dir}")
            
            
# Estructuras de datos de la tabla de constantes
class constant:
    def __init__(self, value, vtype):
        self.value = value
        self.type = vtype
        self.dir = None

    def test_print(self):
        print(f"{self.value} : {self.type}")

class ConstantTable:
    def __init__(self):
        self.constants = {} #diccionario de constantes

    def add_constant(self, value, vtype):
        cons = constant(value, vtype)          
        if cons.value in self.constants:
            return 
        self.constants[cons.value] = cons
        return 


    def test_print(self):
        for constant in self.constants.values():
            constant.test_print()