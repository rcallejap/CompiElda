# Generated from little_duck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

from data_structures import Variable, VarTable, Function, FunctionDirectory, Cuadroplo
from cubo_semantico import check_cubo_semantico

# This class defines a complete generic visitor for a parse tree produced by little_duckParser.


class little_duckVisitor(ParseTreeVisitor):

    def __init__(self, function_directory):
        self.function_directory = function_directory
        self.current_function = 'global'
        self.current_var_table = self.function_directory.global_var_table
        
        self.quad_list = []
        self.current_quad = None
        self.quad_counter = 0
        self.operator_stack = []
        self.operand_stack = []  #lista de PARES (valor y tipo)
        self.jump_stack = []
        self.temp_counter = 0

        self.priority = {
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor1.
    def visitFactor1(self, ctx:little_duckParser.Factor1Context):
        if ctx.ID():
            if self.current_function == 'global':
                name = self.function_directory.global_var_table.variables[ctx.ID().getText()].name
                typ = self.function_directory.global_var_table.variables[ctx.ID().getText()].type
                self.operand_stack.append((name, typ))
            else:
                name = self.function_directory.functions[self.current_function].var_table.variables[ctx.ID().getText()].name
                typ = self.function_directory.functions[self.current_function].var_table.variables[ctx.ID().getText()].type
                self.operand_stack.append((name, typ))
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by little_duckParser#cte.
    def visitCte(self, ctx:little_duckParser.CteContext):
        if ctx.CTE_INT():
            self.operand_stack.append((ctx.getText(), 'int'))      
        elif ctx.CTE_FLOAT():
            self.operand_stack.append((ctx.getText(), 'float'))
        return self.visitChildren(ctx)
    

    
# Operaciones logicas 
    # Visit a parse tree produced by little_duckParser#assign.
    def visitAssign(self, ctx:little_duckParser.AssignContext):
        id = ctx.ID().getText()
        if self.current_function == 'global':
            if id in self.function_directory.global_var_table.variables:
                name = self.function_directory.global_var_table.variables[ctx.ID().getText()].name
                typ = self.function_directory.global_var_table.variables[ctx.ID().getText()].type
                self.operand_stack.append((name, typ))
            else:
                raise Exception('Variable not declared')
                return
        else:
            if id in self.function_directory.functions[self.current_function].var_table.variables:
                name = self.function_directory.global_var_table.variables[ctx.ID().getText()].name
                typ = self.function_directory.global_var_table.variables[ctx.ID().getText()].type
                self.operand_stack.append((name, typ))
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
        if ctx.MAYOR:
            self.operator_stack.append('>')
        elif ctx.MENOR:
            self.operator_stack.append('<')
        elif ctx.DIF:
            self.operator_stack.append('!=')

        return self.visitChildren(ctx)


# Operacion no lineales y print 
 # Visit a parse tree produced by little_duckParser#print.
    def visitPrint(self, ctx:little_duckParser.PrintContext): 
        self.operator_stack.append('PRNT')
        
        return  self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#print0.
    def visitPrint0(self, ctx:little_duckParser.Print0Context):
        self.visitChildren(ctx)
        pop_and_add(self)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#print1.
    def visitPrint1(self, ctx:little_duckParser.Print1Context):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by little_duckParser#cycle.
    def visitCycle(self, ctx:little_duckParser.CycleContext):
        start_loop_quad = self.quad_counter  # Mark the start of the loop
        self.jump_stack.append(start_loop_quad)
        
        self.visit(ctx.body())  # Process the loop body
        
        self.visit(ctx.expression())  # Evaluate the condition
        
        condition_result = self.operand_stack.pop()  # Get the result of the condition
        if condition_result[1] != 'bool':
            raise Exception('Condition expression must be boolean')
        
        end_loop_quad = self.quad_counter  # The quad where we evaluate the condition
        
        # Create a quad for the condition evaluation
        quad = Cuadroplo('GOTOF', condition_result[0], None, None, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1
        
        # Create a quad for jumping back to the start of the loop if the condition is true
        quad = Cuadroplo('GOTO', None, None, start_loop_quad, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1
        
        # Fill the false jump quad with the address of the quad after the loop
        self.quad_list[end_loop_quad].result = self.quad_counter
        
        return self.visitChildren(ctx)


    

    # Visit a parse tree produced by little_duckParser#condition.
    # Visit a parse tree produced by little_duckParser#condition.
def visitCondition(self, ctx: little_duckParser.ConditionContext):
    # Step 1: Evaluate the condition expression
    self.visit(ctx.expression())
    
    # Step 2: Create a quad for the conditional jump
    condition_result = self.operand_stack.pop()
    if condition_result[1] != 'bool':
        raise Exception('Condition expression must be boolean')
    
    quad = Cuadroplo('GOTOF', condition_result[0], None, None, self.current_function)
    self.quad_list.append(quad)
    self.quad_counter += 1
    
    # Save the position of the GOTOF quad to update it later
    false_jump_index = self.quad_counter - 1
    
    # Step 3: Visit the body of the IF statement
    self.visit(ctx.body())
    
    # Step 4: Handle the optional ELSE part
    if ctx.condition0().getChildCount() > 0:
        # Create a GOTO quad for the end of the IF body
        quad = Cuadroplo('GOTO', None, None, None, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1
        
        # Save the position of the GOTO quad to update it later
        end_if_jump_index = self.quad_counter - 1
        
        # Update the GOTOF quad to jump to the ELSE part
        self.quad_list[false_jump_index].result = self.quad_counter
        
        # Visit the body of the ELSE statement
        self.visit(ctx.condition0().body())
        
        # Update the GOTO quad to jump to the end of the ELSE part
        self.quad_list[end_if_jump_index].result = self.quad_counter
    else:
        # If there is no ELSE part, update the GOTOF quad to jump to the end of the IF body
        self.quad_list[false_jump_index].result = self.quad_counter
    
    return self.visitChildren(ctx)


# Visit a parse tree produced by little_duckParser#condition0.
def visitCondition0(self, ctx: little_duckParser.Condition0Context):
    return self.visitChildren(ctx)



    # Visit a parse tree produced by little_duckParser#condition0.
    def visitCondition0(self, ctx:little_duckParser.Condition0Context):
        return self.visitChildren(ctx)



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
        result_type = check_cubo_semantico(operator, left_operand[1], right_operand[1])
        if result_type == 'Error':
            print ('error')
            print (left_operand, right_operand, operator)
            print ( 'Res: ', result_type)
            #raise Exception('Type mismatch')
        cuad = Cuadroplo(operator, right_operand[0], None, left_operand[0], self.current_function)
        self.quad_list.append(cuad)
        self.quad_counter += 1
    elif operator == 'PRNT':
        quad = Cuadroplo(operator, None, None, left_operand[0], self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1
        
    else:
        result_type = check_cubo_semantico(operator, left_operand[1], right_operand[1])
        if result_type == 'Error':
            print ('error')
            print (left_operand, right_operand, operator)
            print ( 'Res: ', result_type)
            #raise Exception('Type mismatch')
        result = 't' + str(self.temp_counter)
        self.temp_counter += 1
        self.operand_stack.append((result, result_type))
        quad = Cuadroplo(operator, left_operand[0], right_operand[0], result, self.current_function)
        self.quad_list.append(quad)
        self.quad_counter += 1


def pop_and_add(self):
    if self.operator_stack[-1] in ('PRNT', 'GOTO', 'GOTOF', 'GOTOV'):
        operator = self.operator_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, None)
        return
    

    operator = self.operator_stack.pop()
    right_operand = self.operand_stack.pop()
    left_operand = self.operand_stack.pop()
    add_cuad(self, operator, left_operand, right_operand)








##Metodos Inutiles 
# Metodo para agregar cuadruplos
def check_and_pop(self, operator):
    
    #if operator has equal or higher precedence than top of stack, pop and generate quad
    print('oper', self.operator_stack)
    print('operand', self.operand_stack)

    while self.operator_stack and self.priority[self.operator_stack[-1]] >= self.priority[operator]:
        operator = self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, right_operand)
        

    
    


def pop_all(self):
    print('*oper', self.operator_stack)
    print('*operand', self.operand_stack)
    while self.operator_stack:
        operator = self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        add_cuad(self, operator, left_operand, right_operand)

