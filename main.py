class TokenType():
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

class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.


class Lexer():

	def __init__(self, program):

		self.program_lines = []

		for count, line in enumerate(program):
			self.program_lines+=[line]
		self.lines = count + 1

		self.token_parser()

	def token_parser(self):
		tokens = []
		for line in self.program_lines:
			for current_token in line.split():
				self.check_token(current_token)


		

	def check_token(self, token):
		if token == "set":
			token_obj = Token(token, TokenType.SET )
		elif token == "SCOPE:":
			token_obj = Token(token, TokenType.SCOPE )
		else:
			self.abort(f'{token} is not valid')

		return token_obj



	def abort(self, error_code):
		print(f'I am Error: {error_code}')
		exit()
	


file = open(r'./test.bz', 'r')

test = Lexer(file)

file.close()
