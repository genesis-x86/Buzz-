import re

class TokenType():

    functions = []

    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords
    SET = 101
    DEF = 102
    START = 103
    END = 104
    INV = 105
    INC = 106
    LOAD = 107
    CDEC = 108
    ARGS = 109
    A = 110
    B = 111
    OUTPUT = 112
    SCOPE = 113
    # Operators
    COLON = 201  
    SEMICOLON = 202
    COMMA = 203
    DASH = 204
    OPENBRACKET = 205
    CLOSEBRACKET = 206
    OPENPARENTHESIS = 207
    CLOSEPARENTHESIS = 208

    def new_function(self, func_name, args, commands):
        pass
        return conversion

class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.
        if self.kind == 102:
            self.usr_function()
    
    def usr_function(self):
        if self.kind == 102:
            return True
        else:
            return False

class Lexer():

    def __init__(self, program):

        self.program_lines = []

        for count, line in enumerate(program):
            self.program_lines+=[line]
        self.lines = count + 1

        self.token_parser()

    def token_parser(self):
        tokens = []
        for self.line in self.program_lines:

            line_str = "".join(self.line)
            operators = "\s|;|:|,|-"
            self.line = re.split(r'(\s|;|:|,|-)', line_str)
            self.line = [i for i in self.line if i != '']
            self.line = [i for i in self.line if i != ' ']
            print(self.line)
            index = 0
            for current_token in self.line:
                token = self.check_token(current_token, index)
                index+=1

    def check_token(self, token, token_index):
        
        if token == "set":
            token_obj = Token(token, TokenType.SET )
        elif token == "SCOPE":
            token_obj = Token(token, TokenType.SCOPE )
        elif token.isnumeric() == True:
            token_obj = Token(token, TokenType.NUMBER )
        elif token == "\n":
            token_obj = Token(token, TokenType.NEWLINE )
        elif token == "A":
            token_obj = Token(token, TokenType.A )
        elif token == "B":
            token_obj = Token(token, TokenType.B )
        elif token == "OUTPUT":
            token_obj = Token(token, TokenType.OUTPUT )
        elif token == "INV":
            token_obj = Token(token, TokenType.INV )
        elif token == "LOAD":
            token_obj = Token(token, TokenType.LOAD )
        elif token == "INC":
            token_obj = Token(token, TokenType.INC )
        elif token == "CDEC":
            token_obj = Token(token, TokenType.CDEC )
        elif token == "START":
            token_obj = Token(token, TokenType.START )
        elif token == "END":
            token_obj = Token(token, TokenType.END )
        elif token == ";":
            token_obj = Token(token, TokenType.SEMICOLON )
        elif token == ":":
            token_obj = Token(token, TokenType.COLON )
        elif token == "-":
            token_obj = Token(token, TokenType.DASH )
        elif token == ",":
            token_obj = Token(token, TokenType.COMMA )






        elif token == "def":
            token_obj = Token(token, TokenType.DEF )
        # Checks for function name
        elif (isinstance(token, str) == True) and (self.line[token_index - 1] == "def"):
            token_obj = Token(token, TokenType.STRING)
            print(token)
        else:
            self.abort(f'{token} is not valid')

        return token_obj

    def abort(self, error_code):
        print(f'I am Error: {error_code}')
        exit()

file = open(r'./test2.bz', 'r')

test = Lexer(file)

file.close()
