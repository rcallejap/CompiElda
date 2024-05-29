'''
'PRNT', 
'GOTO',
'GOTOF',
'GOTOV',
'=',
'!=',
'>',
'<',
'+',
'-',
'*',
'/',
'''

class VirtualMachine:
    def __init__(self, cuads,memory):
        self.cuads = cuads
        self.memory = memory
        self.size = (len(cuads)-1)

    def run(self, debug = False):
        if debug:
            print("memoria inicial: ", self.memory)
            for cuad in self.cuads:
                print(cuad.op, cuad.left, cuad.right, cuad.result)

        currCuad = 0
        while currCuad<= self.size:
            op = self.cuads[currCuad].op
            if op == '=':
                self.igual(self.cuads[currCuad].left, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '+':
                self.suma((self.cuads[currCuad].left), self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '-':
                self.resta(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '*':
                self.multiplicacion(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '/':
                self.division(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '>':
                self.mayor(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '<':
                self.menor(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == '!=':
                self.diferente(self.cuads[currCuad].left, self.cuads[currCuad].right, self.cuads[currCuad].result)
                currCuad+=1
            elif op == 'PRNT':
                self.printCuad(self.cuads[currCuad].result)
                currCuad+=1
            elif op == 'ENDL':
                print("")
                currCuad+=1
            elif op == 'GOTO':
                currCuad = self.goto(self.cuads[currCuad].result)
            elif op == 'GOTOF':
                currCuad = self.gotoF(self.cuads[currCuad].left, self.cuads[currCuad].result, currCuad)
            elif op == 'GOTOV':
                currCuad = self.gotoV(self.cuads[currCuad].left, self.cuads[currCuad].result, currCuad)
            else:
                currCuad+=1

        if debug:
            print("memoria final: ", self.memory)


    def convertMem(self, num):
        num = str(num)
        if len(num) == 4:
            return int(num[0]), int(num[1:4])
        else:
            return int(num[0]), int(num[1:3])

    def checkNone(self, dir):    
        if self.memory[dir[0]][dir[1]] == None:
            raise Exception('Error: NoneType')

    def igual(self, left, result):
        left = self.convertMem(left)
        result = self. convertMem(result)
        self.checkNone(left)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]]

    def suma(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] + self.memory[right[0]][right[1]]

    def resta(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] - self.memory[right[0]][right[1]]
        
    def multiplicacion(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = round(self.memory[left[0]][left[1]] * self.memory[right[0]][right[1]], 8)

    def division(self, left, right, result):
        
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)        
        if result[0] == 1: 
            self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] // self.memory[right[0]][right[1]]
        else:
            self.memory[result[0]][result[1]] = round(self.memory[left[0]][left[1]] / self.memory[right[0]][right[1]], 8)

    def mayor(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] > self.memory[right[0]][right[1]]

    def menor(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] < self.memory[right[0]][right[1]]

    def diferente(self, left, right, result):
        left = self.convertMem(left)
        right = self.convertMem(right)
        result = self. convertMem(result)
        self.checkNone(left)
        self.checkNone(right)
        self.memory[result[0]][result[1]] = self.memory[left[0]][left[1]] != self.memory[right[0]][right[1]]

    def printCuad(self, result):
        result = self.convertMem(result)
        result = self.memory[result[0]][result[1]]
        result = str(result)
        result = result.replace('"', "" )
        print(result, end="")

    def goto(self, result):
        return result
    
    def gotoF(self, left, result, currCuad):
        left = self.convertMem(left)
        if self.memory[left[0]][left[1]] == False:
            return result
        else:
            return currCuad+1
        
    def gotoV(self, left, result, currCuad):
        left = self.convertMem(left)
        if self.memory[left[0]][left[1]] == True:
            return result
        else:
            return currCuad+1
        



        

                