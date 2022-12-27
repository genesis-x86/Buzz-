class CPU:

    # Initializes memory and register arrays
    def __init__(self, memSize=10):

        self.mem = [0 for n in range(memSize)]
        self.memSize = memSize

class State(CPU):

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

print("Welcome to Buzz version 2!")
print(f'Type "help", "credits" or "license" for more information. ')


state = State(20)

# Main loop
while True:

    print(state.mem)
    print(state.returnState())

    operation = input("Buzz > ")
    if operation == "INC":
        state.incReg()
    elif operation == "CDEC":
        state.cdecReg()
    elif operation == "INV":
        state.invMem()
    elif operation == "LOAD":
        state.loadMem()
    elif operation == "license":
        print("Code is available on github. Licensed under GNU")
    elif operation == "credits":
        print("Original woodpecker implementation by radical semiconductor")
        print("Buzz interpretation by project pleiades")
        print("Made by genesis")
    elif operation == "help":
        print("The woodpecker cpu is a zero-indexed array of 2^32 bits of memory, all initialized at zero. The cpu includes a binary memory register which can be accessed at any index in the array.  The cpu allows four operations: INC to increment the index, LOAD which loads the binary memory register with 1, if the memory at the current index is 1, INV which inverts the bit in the memory and CDEC which decrements the register if and only if the bit it has loaded is 1. ")
    else:
        print(f'Woodpecker Error: "{operation}" not valid')

