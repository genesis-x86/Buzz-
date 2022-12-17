import re


class lexer():

    def __init__(self, program):

        self.program_lines = []
        self.program_variables = []
        self.program_functions = []

        for count, line in enumerate(program):
            self.program_lines+=[line]
        self.lines = count + 1

        


    def token_parser(self):
        self.tokens = []
        self.tokens_type = []
        for self.line in self.program_lines:

            line_str = "".join(self.line)
            operators = r'(\s|:|,|\+|#|-|[(|)]|\[|\])'
            self.line = re.split(operators, line_str)
            self.line = [i for i in self.line if i != '']
            self.line = [i for i in self.line if i != ' ']
            #print(self.line)
            index = 0
            for current_token in self.line:
                token = self.check_token(current_token, index)

                if token != None:

                    self.tokens+=[token.text]
                    self.tokens_type+=[token.kind]
                    index+=1
                else:
                    break
            
        print("Successfully parsed program!")
        print(self.tokens)
        return self.tokens, self.tokens_type     

    def check_token(self, token, token_index):
        
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
        
        # Checks for function definition
        elif (isinstance(token, str) == True) and (self.previous_token(token_index) == "let") or (token in self.program_variables):
            token_obj = Token(token, TokenType.IDENT)

            if token not in self.program_variables:
                self.program_variables.append(token_obj.text)

        elif (isinstance(token, str) == True) and (self.line[0] == "def") or (token in self.program_functions):

            token_obj = Token(token, TokenType.IDENT)

            if token not in self.program_functions:
                self.program_functions.append(token_obj.text)
            
        else:
            self.abort(f'Unknown token "{token}" is not valid')
        return token_obj

    def previous_token(self, index):

        try:
            return self.line[index - 1]
        except:
            return None

    def abort(self, error_code):
        print(f'I am Error: {error_code}')
        exit()

class TokenType():

    functions = []

    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2

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
    
    def usr_function(self):
        if self.kind == 102:
            return True
        else:
            return False
