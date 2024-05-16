cubo_semantico ={
     'int': {
        '+': {'int': 'int', 'float': 'float', 'string': 'Error'},
        '-': {'int': 'int', 'float': 'float', 'string': 'Error'},
        '*': {'int': 'int', 'float': 'float', 'string': 'Error'},
        '/': {'int': 'float', 'float': 'float', 'string': 'Error'},
        '>': {'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '<': {'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '!=':{'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '=': {'int': 'int', 'float': 'error', 'string': 'Error'},

    },

    'float': {
        '+': {'int': 'float', 'float': 'float', 'string': 'Error'},
        '-': {'int': 'float', 'float': 'float', 'string': 'Error'},
        '*': {'int': 'float', 'float': 'float', 'string': 'Error'},
        '/': {'int': 'float', 'float': 'float', 'string': 'Error'},
        '>': {'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '<': {'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '!=':{'int': 'bool', 'float': 'bool', 'string': 'Error'},
        '=': {'int': 'error', 'float': 'float', 'string': 'Error'},
    },

    'string': {
        '+': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '-': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '*': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '/': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '>': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '<': {'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '!=':{'int': 'Error', 'float': 'Error', 'string': 'Error'},
        '=': {'int': 'Error', 'float': 'Error', 'string': 'string'},
    }

}




def check_cubo_semantico(op1_tipo, operador, op2_tipo):

    if op1_tipo in cubo_semantico and operador in cubo_semantico[op1_tipo]:
        if op2_tipo in cubo_semantico[op1_tipo][operador]:
            return cubo_semantico[op1_tipo][operador][op2_tipo]
    return 'Error'