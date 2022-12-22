import re

class lexer():
    
    def __init__(self, program):

        self.current_line = ""

        self.line_number = 0

        self.lines = []
        self.tokens = []
        self.variables = []
        self.functions = []
        self.types = []

        for count, line in enumerate(program):
            self.lines+=[line]

    def parse_tokens(self):

        for self.current_line in self.lines:

            self.line_number+=1
            
            operators = r'(\s|:|,|\+|\*|/|#|=|-|[(|)]|\[|\])'
            self.current_line = re.split(operators, self.current_line)
            self.current_line = [i for i in self.current_line if i != '']
            self.current_line = [i for i in self.current_line if i != ' ']
            self.current_line = [i for i in self.current_line if i != '\n']
            self.current_line = [i for i in self.current_line if i != [] ]

            index = 0
            line = []
            line_types = []
            for self.current_token in self.current_line:
                token = self.check_token(self.current_token, index)
                if token != None:
                    line+=[token.text]
                    line_types+=[token.kind]
                    index+=1
                else:
                    break

            self.tokens.append(line)
            self.types.append(line_types)

        return self.tokens, self.types




    def check_token(self, token, token_index):
        #print(self.previous_token(token_index))
        
        if token == "let":
            token_obj = Token(token, TokenType.LET )
        elif token == "def":
            token_obj = Token(token, TokenType.DEF )
        elif token.isnumeric() == True:
            token_obj = Token(token, TokenType.NUMBER )
        elif token == "INV":
            token_obj = Token(token, TokenType.INV )
        elif token == "LOAD":
            token_obj = Token(token, TokenType.LOAD )
        elif token == "INC":
            token_obj = Token(token, TokenType.INC )
        elif token == "CDEC":
            token_obj = Token(token, TokenType.CDEC )
        elif token == "=":
            token_obj = Token(token, TokenType.EQUAL )
        elif token == ":":
            token_obj = Token(token, TokenType.COLON )
        elif token == "-":
            token_obj = Token(token, TokenType.MINUS )
        elif token == "+":
            token_obj = Token(token, TokenType.PLUS )
        elif token == "*":
            token_obj = Token(token, TokenType.MULTIPLY )
        elif token == "/":
            token_obj = Token(token, TokenType.DIVIDE )
        elif token == ",":
            token_obj = Token(token, TokenType.COMMA )
        elif token == "(":
            token_obj = Token(token, TokenType.OPENPARENTHESIS )
        elif token == ")":
            token_obj = Token(token, TokenType.CLOSEPARENTHESIS )
        elif token == "[":
            token_obj = Token(token, TokenType.OPENBRACKET )
        elif token == "]":
            token_obj = Token(token, TokenType.CLOSEBRACKET )
        elif token == "\n":
            token_obj = Token(token, TokenType.NEWLINE )
        elif token == "#":
            return None
        # Checks for variable definition
        elif (isinstance(token, str) == True) and (self.previous_token(token_index) == "let") or (token in self.variables):
            token_obj = Token(token, TokenType.IDENT)

            if token not in self.variables:
                self.variables.append(token_obj.text)

        elif (isinstance(token, str) == True) and (self.current_line[0] == "def") or (token in self.functions):

            token_obj = Token(token, TokenType.IDENT)

            if token not in self.functions:
                self.functions.append(token_obj.text)
                
            
        else:
            self.abort(f'Unknown token in line {self.line_number}: "{token}" is not valid')
        return token_obj

    def previous_token(self, index):

        try:
            return self.current_line[index - 1]
        except:
            return None

    def next_token(self, index):

        try:
            return self.current_line[index + 1]
        except:
            return None



    def abort(self, error_code):
        print(f'Buzz Error: {error_code}')
        exit()

class TokenType():

    functions = []

    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    FUNC = 3

    # Keywords
    LET = 101
    DEF = 102
    ARGS = 103

    # Operations
    CDEC = 201
    INC = 202
    INV = 203
    LOAD = 204
    
    # Binary Operators
    EQUAL = 301  
    PLUS = 302
    MINUS = 303
    DIVIDE = 305
    MULTIPLY = 306

    # Grammar
    COMMA = 401
    OPENBRACKET = 402
    CLOSEBRACKET = 403
    OPENPARENTHESIS = 404
    CLOSEPARENTHESIS = 405
    COLON = 406

class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.
    