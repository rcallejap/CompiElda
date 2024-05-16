from data_structures import Variable, VarTable, Function, FunctionDirectory

# Create a FunctionDirectory object
fd = FunctionDirectory()

# Create a Variable object
v1 = Variable("x", "int", 10)
v2 = Variable("y", "float", 3.14)
v3 = Variable("z", "string", "hello")

# Add the variables to the global variable table
fd.add_variable(v1, "global")

# Add a function to the function directory
fd.add_function("main")

# Add a variable to the function's variable table
fd.add_variable(v2, "main")

# Add another function to the function directory
fd.add_function("foo")

# Add a variable to the function's variable table
fd.add_variable(v3, "foo")


# Print the contents of the function directory
fd.test_print()


