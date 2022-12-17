import argparse
from Lexer.lexer import lexer

class buzz_parser():

    def __init__(self):
        pass

    def parse_statements(self, program_tokens, program_types):

        statements = []
        statements_kind = []
        current_statement = []
        current_statement_types = []
        index = 0
        for current_token in program_tokens:

            #print(f'Current token: {current_token}')
            
            if current_token != "\n":
                current_statement.append(current_token)
                current_statement_types.append(program_types[index])
            else:
                current_statement.append(current_token)
                current_statement_types.append(program_types[index])
                statements_kind+=[current_statement_types]
                statements+=[current_statement]
                current_statement = []
                current_statement_types = []
            index+=1


        return statements, statements_kind


    def match(self, statement_types):

        self.environment_variables = ["A", "B", "OUTPUT"]
        
        for line in statement_types:
            index = 0
            for current_token in line:

                try:
                    next_token = line[index + 1]

                except:
                    next_token = None


                index+=1

            

            
                

            

        
def main():
        
    parser = argparse.ArgumentParser(description="Buzz! programming language parser for Woodpecker CPU")
    parser.add_argument('filename')
    args = parser.parse_args()

    with open(args.filename) as file:
        program = lexer(file)

        program_tokens, program_types = program.token_parser()

        #print(f'DEBUG{program_types}')
        test = buzz_parser()
        statements, statement_types = test.parse_statements(program_tokens, program_types)
        test.match(statement_types)


if __name__=="__main__":
    main()