#DFTV2-PN: Directorio de funciones y tablas de variables entrega 2 Puntos Neuralgicos
#DFTV2-PN:  1: Creacion vareables 
#DFTV2-PN:  2: Se agrega el nombre de la variable a la lista de variables actuales
#DFTV2-PN:  3: Se asigna el tipo de variable a la variable current_type y se agregan las variables a la tabla de variables de la funcion actual y al terminar se eliminan la lista de variables actuales
#DFTV2-PN:  4: Entrando a FUNCS se crea una nueva funcion en el directorio de funciones y se asigna a la variable current_function
#DFTV2-PN:  5: Saliendo de FUNCS se limpia la variable current_function
#DFTV2-PN:  6: print de prueba para mostrar el contenido del directorio de funciones y las variables de cada funcion


# Generated from little_duck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

from data_structures import Variable, VarTable, Function, FunctionDirectory


# This class defines a complete listener for a parse tree produced by little_duckParser.
class little_duckListener(ParseTreeListener):
    
    #DFTV2-PN:  1
    def __init__(self):
        self.function_directory = FunctionDirectory()
        self.current_function = ""
        self.current_type = None
        self.current_var_arr = []


    #DFTV2-PN:  1
    # Enter a parse tree produced by little_duckParser#start_.
    def enterStart_(self, ctx:little_duckParser.Start_Context):
        self.current_function = "global" 
        pass

    #DFTV2-PN:  6
    # Exit a parse tree produced by little_duckParser#start_.
    def exitStart_(self, ctx:little_duckParser.Start_Context):
        #self.function_directory.test_print()
        pass

    #DFTV2-PN:  2
    # Exit a parse tree produced by little_duckParser#var1.
    def exitVar1(self, ctx:little_duckParser.Var1Context):
        varname = ctx.ID().getText()
        self.current_var_arr.append(varname)
        pass

    #DFTV2-PN:  3
    # Exit a parse tree produced by little_duckParser#type.
    def exitType(self, ctx:little_duckParser.TypeContext):
        self.current_type = ctx.getText()   
        for varname in self.current_var_arr:
            self.function_directory.add_variable(Variable(varname, self.current_type), self.current_function)
        self.current_var_arr = []
        pass

    #DFTV2-PN:  4
    # Enter a parse tree produced by little_duckParser#funcs.
    def enterFuncs(self, ctx:little_duckParser.FuncsContext):
        funcName = ctx.ID().getText()
        self.function_directory.add_function(funcName)
        self.current_function = funcName

        pass

    #DFTV2-PN:  5
    # Exit a parse tree produced by little_duckParser#funcs.
    def exitFuncs(self, ctx:little_duckParser.FuncsContext):
        self.current_function = "global"
        pass




    '''no usadas todavia '''
    # Enter a parse tree produced by little_duckParser#vars.
    def enterVars(self, ctx:little_duckParser.VarsContext):
    
        pass

    # Exit a parse tree produced by little_duckParser#vars.
    def exitVars(self, ctx:little_duckParser.VarsContext):

        pass

    # Enter a parse tree produced by little_duckParser#var0.
    def enterVar0(self, ctx:little_duckParser.Var0Context):
        pass

    # Exit a parse tree produced by little_duckParser#var0.
    def exitVar0(self, ctx:little_duckParser.Var0Context):
        pass


    # Enter a parse tree produced by little_duckParser#var1.
    def enterVar1(self, ctx:little_duckParser.Var1Context):
        pass

    # Enter a parse tree produced by little_duckParser#var2.
    def enterVar2(self, ctx:little_duckParser.Var2Context):
        pass

    # Exit a parse tree produced by little_duckParser#var2.
    def exitVar2(self, ctx:little_duckParser.Var2Context):
        pass


    # Enter a parse tree produced by little_duckParser#type.
    def enterType(self, ctx:little_duckParser.TypeContext):
        pass

    # Enter a parse tree produced by little_duckParser#body.
    def enterBody(self, ctx:little_duckParser.BodyContext):
        pass

    # Exit a parse tree produced by little_duckParser#body.
    def exitBody(self, ctx:little_duckParser.BodyContext):
        pass


    # Enter a parse tree produced by little_duckParser#statement.
    def enterStatement(self, ctx:little_duckParser.StatementContext):
        pass

    # Exit a parse tree produced by little_duckParser#statement.
    def exitStatement(self, ctx:little_duckParser.StatementContext):
        pass


    # Enter a parse tree produced by little_duckParser#assign.
    def enterAssign(self, ctx:little_duckParser.AssignContext):
        pass

    # Exit a parse tree produced by little_duckParser#assign.
    def exitAssign(self, ctx:little_duckParser.AssignContext):
        pass


    # Enter a parse tree produced by little_duckParser#print.
    def enterPrint(self, ctx:little_duckParser.PrintContext):
        pass

    # Exit a parse tree produced by little_duckParser#print.
    def exitPrint(self, ctx:little_duckParser.PrintContext):
        pass


    # Enter a parse tree produced by little_duckParser#print0.
    def enterPrint0(self, ctx:little_duckParser.Print0Context):
        pass

    # Exit a parse tree produced by little_duckParser#print0.
    def exitPrint0(self, ctx:little_duckParser.Print0Context):
        pass


    # Enter a parse tree produced by little_duckParser#print1.
    def enterPrint1(self, ctx:little_duckParser.Print1Context):
        pass

    # Exit a parse tree produced by little_duckParser#print1.
    def exitPrint1(self, ctx:little_duckParser.Print1Context):
        pass


    # Enter a parse tree produced by little_duckParser#cycle.
    def enterCycle(self, ctx:little_duckParser.CycleContext):
        pass

    # Exit a parse tree produced by little_duckParser#cycle.
    def exitCycle(self, ctx:little_duckParser.CycleContext):
        pass


    # Enter a parse tree produced by little_duckParser#condition.
    def enterCondition(self, ctx:little_duckParser.ConditionContext):
        pass

    # Exit a parse tree produced by little_duckParser#condition.
    def exitCondition(self, ctx:little_duckParser.ConditionContext):
        pass


    # Enter a parse tree produced by little_duckParser#condition0.
    def enterCondition0(self, ctx:little_duckParser.Condition0Context):
        pass

    # Exit a parse tree produced by little_duckParser#condition0.
    def exitCondition0(self, ctx:little_duckParser.Condition0Context):
        pass


    # Enter a parse tree produced by little_duckParser#expression.
    def enterExpression(self, ctx:little_duckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by little_duckParser#expression.
    def exitExpression(self, ctx:little_duckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by little_duckParser#expression0.
    def enterExpression0(self, ctx:little_duckParser.Expression0Context):
        pass

    # Exit a parse tree produced by little_duckParser#expression0.
    def exitExpression0(self, ctx:little_duckParser.Expression0Context):
        pass


    # Enter a parse tree produced by little_duckParser#expression1.
    def enterExpression1(self, ctx:little_duckParser.Expression1Context):
        pass

    # Exit a parse tree produced by little_duckParser#expression1.
    def exitExpression1(self, ctx:little_duckParser.Expression1Context):
        pass


    # Enter a parse tree produced by little_duckParser#exp.
    def enterExp(self, ctx:little_duckParser.ExpContext):
        pass

    # Exit a parse tree produced by little_duckParser#exp.
    def exitExp(self, ctx:little_duckParser.ExpContext):
        pass


    # Enter a parse tree produced by little_duckParser#exp0.
    def enterExp0(self, ctx:little_duckParser.Exp0Context):
        pass

    # Exit a parse tree produced by little_duckParser#exp0.
    def exitExp0(self, ctx:little_duckParser.Exp0Context):
        pass


    # Enter a parse tree produced by little_duckParser#exp1.
    def enterExp1(self, ctx:little_duckParser.Exp1Context):
        pass

    # Exit a parse tree produced by little_duckParser#exp1.
    def exitExp1(self, ctx:little_duckParser.Exp1Context):
        pass


    # Enter a parse tree produced by little_duckParser#cte.
    def enterCte(self, ctx:little_duckParser.CteContext):
        pass

    # Exit a parse tree produced by little_duckParser#cte.
    def exitCte(self, ctx:little_duckParser.CteContext):
        pass


    # Enter a parse tree produced by little_duckParser#termino.
    def enterTermino(self, ctx:little_duckParser.TerminoContext):
        pass

    # Exit a parse tree produced by little_duckParser#termino.
    def exitTermino(self, ctx:little_duckParser.TerminoContext):
        pass


    # Enter a parse tree produced by little_duckParser#termino0.
    def enterTermino0(self, ctx:little_duckParser.Termino0Context):
        pass

    # Exit a parse tree produced by little_duckParser#termino0.
    def exitTermino0(self, ctx:little_duckParser.Termino0Context):
        pass


    # Enter a parse tree produced by little_duckParser#termino1.
    def enterTermino1(self, ctx:little_duckParser.Termino1Context):
        pass

    # Exit a parse tree produced by little_duckParser#termino1.
    def exitTermino1(self, ctx:little_duckParser.Termino1Context):
        pass


    # Enter a parse tree produced by little_duckParser#factor.
    def enterFactor(self, ctx:little_duckParser.FactorContext):
        pass

    # Exit a parse tree produced by little_duckParser#factor.
    def exitFactor(self, ctx:little_duckParser.FactorContext):
        pass


    # Enter a parse tree produced by little_duckParser#factor0.
    def enterFactor0(self, ctx:little_duckParser.Factor0Context):
        pass

    # Exit a parse tree produced by little_duckParser#factor0.
    def exitFactor0(self, ctx:little_duckParser.Factor0Context):
        pass


    # Enter a parse tree produced by little_duckParser#factor1.
    def enterFactor1(self, ctx:little_duckParser.Factor1Context):
        pass

    # Exit a parse tree produced by little_duckParser#factor1.
    def exitFactor1(self, ctx:little_duckParser.Factor1Context):
        pass

    # Enter a parse tree produced by little_duckParser#funcs0.
    def enterFuncs0(self, ctx:little_duckParser.Funcs0Context):
        pass

    # Exit a parse tree produced by little_duckParser#funcs0.
    def exitFuncs0(self, ctx:little_duckParser.Funcs0Context):
        pass


    # Enter a parse tree produced by little_duckParser#funcs1.
    def enterFuncs1(self, ctx:little_duckParser.Funcs1Context):
        pass

    # Exit a parse tree produced by little_duckParser#funcs1.
    def exitFuncs1(self, ctx:little_duckParser.Funcs1Context):
        pass


    # Enter a parse tree produced by little_duckParser#funcs2.
    def enterFuncs2(self, ctx:little_duckParser.Funcs2Context):
        pass

    # Exit a parse tree produced by little_duckParser#funcs2.
    def exitFuncs2(self, ctx:little_duckParser.Funcs2Context):
        pass


    # Enter a parse tree produced by little_duckParser#funcs3.
    def enterFuncs3(self, ctx:little_duckParser.Funcs3Context):
        pass

    # Exit a parse tree produced by little_duckParser#funcs3.
    def exitFuncs3(self, ctx:little_duckParser.Funcs3Context):
        pass


    # Enter a parse tree produced by little_duckParser#f_call.
    def enterF_call(self, ctx:little_duckParser.F_callContext):
        pass

    # Exit a parse tree produced by little_duckParser#f_call.
    def exitF_call(self, ctx:little_duckParser.F_callContext):
        pass


    # Enter a parse tree produced by little_duckParser#f_call0.
    def enterF_call0(self, ctx:little_duckParser.F_call0Context):
        pass

    # Exit a parse tree produced by little_duckParser#f_call0.
    def exitF_call0(self, ctx:little_duckParser.F_call0Context):
        pass


    # Enter a parse tree produced by little_duckParser#f_call1.
    def enterF_call1(self, ctx:little_duckParser.F_call1Context):
        pass

    # Exit a parse tree produced by little_duckParser#f_call1.
    def exitF_call1(self, ctx:little_duckParser.F_call1Context):
        pass


    # Enter a parse tree produced by little_duckParser#f_call2.
    def enterF_call2(self, ctx:little_duckParser.F_call2Context):
        pass

    # Exit a parse tree produced by little_duckParser#f_call2.
    def exitF_call2(self, ctx:little_duckParser.F_call2Context):
        pass



del little_duckParser