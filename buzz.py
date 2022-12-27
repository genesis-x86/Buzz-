import argparse
from Lexer.lexer import lexer
from Parser.parser import parse
from Emitter.emitter import emitter


class CPU:

    # Initializes memory and register arrays
    def __init__(self, memSize=10):

        self.mem = [0 for n in range(memSize)]
        self.memSize = memSize

class State(CPU):

    functions = {}
    variables = {}

    def __init__(self, memSize):
        super().__init__(memSize)

        self.register = 0
        self.memory = self.mem[self.register]
        self.save = 0

    def incReg(self):
        if self.register >= self.memSize - 1:
            self.register = 0
            self.memory = self.mem[0]

        else:
            self.register+=1
        
            self.memory = self.mem[self.register]

    def cdecReg(self):
        
        if self.save == 1 and self.register > 0:
            self.register-=1
            self.memory = self.mem[self.register]
        elif self.save == 1 and self.register <= 0:
            self.register = self.memSize - 1
            self.memory = self.mem[self.register]

    def invMem(self):
        if self.memory == 1:
            self.memory = 0
        else:
            self.memory = 1
        
        self.mem[self.register] = self.memory

    def loadMem(self):

        if self.memory == 1:
            self.save = 1
        else:
            self.save = 0

    def returnState(self):
        return self.register, self.memory, self.save


print("Welcome to Buzz version 3!")
print(f'Type "help", "credits" or "license" for more information. ')


state = State(20)
print(state.returnState())

# Main loop
while True:
    
    statement = input("Buzz > ")

    if statement == "license":
        print("Code is available on github. Licensed under GNU")
    elif statement == "credits":
        print("Original woodpecker implementation by radical semiconductor")
        print("Buzz interpretation by project pleiades")
        print("Made by genesis")
    elif statement == "help":
        print("The woodpecker cpu is a zero-indexed array of 2^32 bits of memory, all initialized at zero. The cpu includes a binary memory register which can be accessed at any index in the array.  The cpu allows four operations: INC to increment the index, LOAD which loads the binary memory register with 1, if the memory at the current index is 1, INV which inverts the bit in the memory and CDEC which decrements the register if and only if the bit it has loaded is 1. ")
    elif statement == "exit":
        exit()
    elif statement == "mem":
        print(state.mem)
    else:
        program = lexer(statement, statement=True, functions=list(state.functions.keys()),variables=list(state.variables.keys()))

        program_tokens, program_types = program.parse_tokens()

        parsed_program = parse(program_tokens, state.functions, state.variables)

        state.functions.update(parsed_program.functions)
        state.variables.update(parsed_program.variables)
        
        emit = emitter(parsed_program.emit())
        print(list(emit.instructions))
        for operation in list(emit.instructions):
            if operation == "INV":
                state.invMem()
            elif operation == "LOAD":
                state.loadMem()
            elif operation == "INC":
                state.incReg()
            elif operation == "CDEC":
                state.cdecReg()
            
        print(state.returnState())

