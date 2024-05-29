# Generated from little_duck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

from data_structures import Variable, VarTable, Function, FunctionDirectory, Cuadruplo
from cubo_semantico import check_cubo_semantico

# This class defines a complete generic visitor for a parse tree produced by little_duckParser.


class little_duckVisitor(ParseTreeVisitor):

    def __init__(self, function_directory, constant_directory, memMan):
        self.function_directory = function_directory
        self.current_function = 'global'
        self.current_var_table = self.function_directory.global_var_table
        self.constant_directory = constant_directory

        self.memorryCountA = memMan 

        
        self.quad_list = []
        self.current_quad = None
        self.quad_counter = 0
        self.operator_stack = []
        self.operand_stack = []  #lista de PARES (valor y tipo)
        self.jump_stack = []
        self.temp_counter = 0

        self.priority = {
            'ENDL': 0, 
            'PRNT':0, 
            'GOTO':0,
            'GOTOF':0,
            'GOTOV':0,
            '=': 0,
            '!=': 1,
            '>': 1,
            '<': 1,
            '+': 2,
            '-': 2,
            '*': 3,
            '/': 3,
        }


# Operaciones aritmeticas 

    # Visit a parse tree produced by little_duckParser#exp.
    def visitExp(self, ctx:little_duckParser.ExpContext):
        self.visit(ctx.termino())
        if self.operator_stack:
            if self.operator_stack[-1] == '+' or self.operator_stack[-1] == '-':
                pop_and_add(self)
        self.visit(ctx.exp0())
        return 


    # Visit a parse tree produced by little_duckParser#exp0.
    def visitExp0(self, ctx:little_duckParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#exp1.
    def visitExp1(self, ctx:little_duckParser.Exp1Context):
        if ctx.MENOS():
            self.operator_stack.append('-')
        elif ctx.MAS():
            self.operator_stack.append('+')

        return self.visitChildren(ctx)



    # Visit a parse tree produced by little_duckParser#termino.
    def visitTermino(self, ctx:little_duckParser.TerminoContext):
        self.visit(ctx.factor())
        if self.operator_stack:
            if self.operator_stack[-1] == '*' or self.operator_stack[-1] == '/':
                pop_and_add(self)
        self.visit(ctx.termino0())
        return 


    # Visit a parse tree produced by little_duckParser#termino0.
    def visitTermino0(self, ctx:little_duckParser.Termino0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#termino1.
    def visitTermino1(self, ctx:little_duckParser.Termino1Context):
        if ctx.POR():
            self.operator_stack.append('*')
        elif ctx.DIV():
            self.operator_stack.append('/') 

        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor.
    def visitFactor(self, ctx:little_duckParser.FactorContext):
        if ctx.PARI():
            self.operator_stack.append('(')
            self.visit(ctx.expression())
            self.operator_stack.pop()
            return 
        else :
            return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor0.
    def visitFactor0(self, ctx:little_duckParser.Factor0Context):
        if ctx.MENOS():
            self.operator_stack.append('-')
        else :
            self.operator_stack.append('+')        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor1.
    def visitFactor1(self, ctx:little_duckParser.Factor1Context):
        if ctx.ID():
            if self.current_function == 'global':
                var = self.function_directory.global_var_table.variables[ctx.ID().getText()]

            else:
                var = self.function_directory.functions[self.current_function].var_table.variables[ctx.ID().getText()]    
            
            cero = self.constant_directory.constants[0]
            self.operand_stack.append(cero)
            self.operand_stack.append(var)
            pop_and_add(self)
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by little_duckParser#cte.
    def visitCte(self, ctx:little_duckParser.CteContext):
        if ctx.CTE_INT():
            var = self.constant_directory.constants[ctx.CTE_INT().getText()]
        elif ctx.CTE_FLOAT():
            var = self.constant_directory.constants[ctx.CTE_FLOAT().getText()]
        
        cero = self.constant_directory.constants[0]
        self.operand_stack.append(cero)
        self.operand_stack.append(var)
        pop_and_add(self)

        return self.visitChildren(ctx)
    

    
# Operaciones logicas 
    # Visit a parse tree produced by little_duckParser#assign.
    def visitAssign(self, ctx:little_duckParser.AssignContext):
        id = ctx.ID().getText()
        if self.current_function == 'global':
            if id in self.function_directory.global_var_table.variables:
                var = self.function_directory.global_var_table.variables[id]
                self.operand_stack.append(var)
            else:
                raise Exception('Variable not declared')
                return
        else:
            if id in self.function_directory.functions[self.current_function].var_table.variables:
                var = self.function_directory.functions[self.current_function].var_table.variables[id]
                self.operand_stack.append(var)
            else:
                raise Exception('Variable not declared')
        
        if ctx.IGUAL():
            self.operator_stack.append('=')
            self.visit(ctx.expression())
            pop_and_add(self)
        return  


     # Visit a parse tree produced by little_duckParser#expression.
    
    def visitExpression(self, ctx:little_duckParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#expression0.
    def visitExpression0(self, ctx:little_duckParser.Expression0Context):
        self.visitChildren(ctx)
        if self.operator_stack:
            if self.operator_stack[-1] == '>' or self.operator_stack[-1] == '<' or self.operator_stack[-1] == '!=':
                pop_and_add(self)        
        return 


    # Visit a parse tree produced by little_duckParser#expression1.
    def visitExpression1(self, ctx:little_duckParser.Expression1Context):
        if ctx.MAYOR():
            self.operator_stack.append('>')
        elif ctx.MENOR():
            self.operator_stack.append('<')
        elif ctx.DIF():
            self.operator_stack.append('!=')

        return self.visitChildren(ctx)


# Operacion no lineales y print 
 # Visit a parse tree produced by little_duckParser#print.
    def visitPrint(self, ctx:little_duckParser.PrintContext): 
        self.visitChildren(ctx)
        printStack = []

        while self.operator_stack and self.operator_stack[-1] == 'PRNT':
            printStack.append(self.operand_stack.pop())
            self.operator_stack.pop()
        for i in range(len(printStack)):
            self.operand_stack.append(printStack.pop())
            self.operator_stack.append('PRNT')
            pop_and_add(self)

        self.operator_stack.append('ENDL')
        pop_and_add(self)

    

        return  


    # Visit a parse tree produced by little_duckParser#print0.
    def visitPrint0(self, ctx:little_duckParser.Print0Context):
        '''if ctx.CTE_STRING():
            self.operand_stack.append((ctx.CTE_STRING().getText(), 'string'))'''
        if ctx.CTE_STRING():
            self.operand_stack.append(self.constant_directory.constants[ctx.CTE_STRING().getText()])
        self.visitChildren(ctx)
        self.operator_stack.append('PRNT')
        return 


    # Visit a parse tree produced by little_duckParser#print1.
    def visitPrint1(self, ctx:little_duckParser.Print1Context):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by little_duckParser#cycle.
    def visitCycle(self, ctx:little_duckParser.CycleContext):
        self.jump_stack.append(self.quad_counter)
        self.visit(ctx.body())
        self.visit(ctx.expression())
        self.operator_stack.append('GOTOV')
        pop_and_add(self)        

        return 


    

    # Visit a parse tree produced by little_duckParser#condition.
    # Visit a parse tree produced by little_duckParser#condition.
    def visitCondition(self, ctx: little_duckParser.ConditionContext):
        self.visit(ctx.expression())

        self.operator_stack.append('GOTOF')
        pop_and_add(self)
        self.jump_stack.append(self.quad_counter - 1)

        self.visit(ctx.body())
        self.visit(ctx.condition0())

        jump = self.jump_stack.pop()        
        self.quad_list[jump].result = self.quad_counter
        return 


    # Visit a parse tree produced by little_duckParser#condition0.
    def visitCondition0(self, ctx: little_duckParser.Condition0Context):
        if ctx.ELSE():
            self.operator_stack.append('GOTO')
            pop_and_add(self)

            jump = self.jump_stack.pop()        
            self.quad_list[jump].result = self.quad_counter

            self.jump_stack.append(self.quad_counter - 1)
            self.visit(ctx.body())
        return 



#Otros metodos



    # Visit a parse tree produced by little_duckParser#start_.
    def visitStart_(self, ctx:little_duckParser.Start_Context):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#vars.
    def visitVars(self, ctx:little_duckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#var0.
    def visitVar0(self, ctx:little_duckParser.Var0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#var1.
    def visitVar1(self, ctx:little_duckParser.Var1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#var2.
    def visitVar2(self, ctx:little_duckParser.Var2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#type.
    def visitType(self, ctx:little_duckParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#body.
    def visitBody(self, ctx:little_duckParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#statement.
    def visitStatement(self, ctx:little_duckParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs.
    def visitFuncs(self, ctx:little_duckParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs0.
    def visitFuncs0(self, ctx:little_duckParser.Funcs0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs1.
    def visitFuncs1(self, ctx:little_duckParser.Funcs1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs2.
    def visitFuncs2(self, ctx:little_duckParser.Funcs2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs3.
    def visitFuncs3(self, ctx:little_duckParser.Funcs3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call.
    def visitF_call(self, ctx:little_duckParser.F_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call0.
    def visitF_call0(self, ctx:little_duckParser.F_call0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call1.
    def visitF_call1(self, ctx:little_duckParser.F_call1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call2.
    def visitF_call2(self, ctx:little_duckParser.F_call2Context):
        return self.visitChildren(ctx)





del little_duckParser

def add_cuad(self, operator, left_operand, right_operand):
    if operator == '=':
        result_type = check_cubo_semantico(operator, left_operand.type , right_operand.type)
        if result_type == 'Error':
            raise Exception('Type mismatch: canot assign' + left_operand.type + 'to' + right_operand.type)
        cuad = Cuadruplo(operator, right_operand.dir, None, left_operand.dir, self.current_function)
        self.quad_list.append(cuad)
        self.quad_counter += 1


    elif operator == 'ENDL':
        quad = Cuadruplo(operator, None, None, None, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1

    elif operator == 'PRNT':
        quad = Cuadruplo(operator, None, None, left_operand.dir, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1

    elif operator == 'GOTO':
        quad = Cuadruplo(operator, None, None, None, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1

    elif operator == 'GOTOV':
        jump = self.jump_stack.pop()
        quad = Cuadruplo(operator, left_operand.dir, None, jump, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1

    elif operator == 'GOTOF':
        quad = Cuadruplo(operator, left_operand.dir, None, None, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1

        
    else:
        result_type = check_cubo_semantico(operator, left_operand.type, right_operand.type)
        if result_type == 'Error':
            raise Exception('Type mismatch')

        dir =0 
        if result_type== 'int':
            dir = self.memorryCountA[0] + 1000
            self.memorryCountA[0] += 1
        elif result_type == 'float':
            dir = self.memorryCountA[1] + 2000
            self.memorryCountA[1] += 1
        elif result_type == 'bool':
            dir = self.memorryCountA[2] + 3000
            self.memorryCountA[2] += 1
        elif result_type == 'string':
            dir = self.memorryCountA[3] + 4000
            self.memorryCountA[3] += 1

        self.temp_counter += 1
        self.function_directory.add_variable(dir, result_type, self.current_function)

        if self.current_function == 'global':
            self.function_directory.global_var_table.variables[dir].dir = dir
        else:
            self.function_directory.functions[self.current_function].var_table.variables[dir].dir = dir

            

        var = self.current_var_table.variables[dir]

        self.operand_stack.append(var)
        #Borrar esto
        #var = var.dir, ':', var.type, '=', var.dir

        quad = Cuadruplo(operator, left_operand.dir, right_operand.dir, var.dir, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1


def pop_and_add(self):
    if self.operator_stack[-1] == 'GOTO':
        operator = self.operator_stack.pop()
        add_cuad(self, operator, None, None)
        return
    
    elif self.operator_stack[-1] == 'PRNT' or self.operator_stack[-1] == 'GOTOV':
        operator = self.operator_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, None)
        return
    
    elif self.operator_stack[-1] == 'GOTOF':
        operator = self.operator_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, None)
        return
    
    elif self.operator_stack[-1] == 'ENDL':
        operator = self.operator_stack.pop()
        add_cuad(self, operator, None, None)
        return


    else: 
        operator = self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, right_operand)
