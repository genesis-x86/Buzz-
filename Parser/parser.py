from pprint import pprint

from Lexer.lexer import lexer

class rparse():
    def __init__(self,functions, variables) -> None:
 
        self.line_number = 0
        self.functions = functions
        self.variables = variables
        self.operations = ["INV", "INC", "CDEC", "LOAD"]


    # Returns a list of woodpecker operations that the recursive function corresponds to
    def recursive_function(self, n, statement):

        output = []

        # Checks for nested recursive operations
        index=0
        n_buffer = -1
        done=False
        for command in statement:

            if command in self.operations and index>n_buffer:
                output.append(command)    

            elif command in self.functions and index>n_buffer:
                output.append(self.functions[command])

            elif command.isnumeric() or command in self.variables:
                if statement[index+1] != "(":
                    self.abort(f'Error in line {self.line_number}: Expected "(" got "{command}"')

                pairs=0
                recursive_operation = []
                n_buffer = index+2
                for operation in statement[index+2:]:                        
                        
                    if operation == ")" and pairs == 0:
                        done = True
                        break

                    elif operation == "(":
                        pairs+=1
                        recursive_operation.append(operation)
                    elif operation == ")" and pairs != 0:
                        pairs-=1
                        recursive_operation.append(operation)
                    elif operation != ",":
                        recursive_operation.append(operation) 

                    n_buffer+=1

                
                test = rparse(self.functions, self.variables)
                
                output.append(test.recursive_function(command, recursive_operation))

            if done == True:
                break
            index+=1

        return output * int(n)

     
class parse():

    def __init__(self, tokens, types) -> None:

        self.line_number = 0
        self.tokens = tokens
        self.types = types
        self.functions = {}
        self.variables = {}
        self.operations = ["INV", "INC", "CDEC", "LOAD"]

        self.emitted_code = []

        self.program()


    def program(self):
        #print("PROGRAM")
        for statement in self.tokens:
            self.line_number+=1
            self.statement(statement)

    def statement(self, statement):

        index = 0
        for self.current_token in statement:


            if self.current_token in self.functions:
                self.emitted_code.append(self.functions[self.current_token])
                
            elif self.current_token in self.operations:
                self.emitted_code.append(self.current_token)
            elif self.current_token.isnumeric() or self.current_token in list(self.variables.keys()):
                
                self.emitted_code.append(self.operational_statement(statement))
                break
                




            elif self.current_token == "let":
                #print("STATEMENT-LET")
                self.variable_definition(statement)
                break
                
            elif self.current_token == "def":
                self.function_definition(statement)
                break
                
            
                

            index+=1

        
    def variable_definition(self, statement):

        if statement.pop(0) == "let":
            EQ = statement.pop(1)
            if EQ == "=":
                variable = statement.pop(0)
                if variable not in self.variables:
                    self.variables[variable] = None

                    if (len(statement) == 1) and (statement[0].isnumeric() == True):
                        #print("NUMBER")
                        self.variables[variable] = statement[0]
                    else:
                        self.variables[variable] = self.expression(statement)
                else:
                    self.variables[variable] = self.expression(statement)
            
            else:
                self.abort(f'Error in line {self.line_number}: Expected "=" got "{EQ}"')
        else:
            self.abort(f'Error in line {self.line_number}: Cannot have a statement within a statement')

    def function_definition(self, statement):
        #print("FUNCTION DEFINITION")
        statement.pop(0)

        if statement[1] == "(":
            ident = statement[2]
            #print(f'Complex function {ident}')
            self.abort("Version Error: Complex functions are not implemented")
        else:

            ident = statement.pop(0)
            #print(f'SIMPLE FUNCTION {ident}')

            self.functions[ident] = None

            if statement.pop(0) != ":":
                self.abort(f'Error in line {self.line_number}: Expected ":" got "{statement[1]}"')

        self.functions[ident] = self.operational_statement(statement)

            

    # Returns a list of the
    def operational_statement(self, statement):
        #print("OPERATIONAL STATEMENT")
        #print(statement)
        n_buffer = -1
        commands = []
        index=0
        done=False

        for operation in statement:


            if operation in self.operations and index>n_buffer:
                commands.append(operation)

            elif operation in self.functions:
                commands.append(self.functions[operation])
    
            # Checks if the function contains a recursive operation
            elif operation.isnumeric() or operation in self.variables:

                if statement.count('(') != statement.count(')'):
                    self.abort(f'Error in line {self.line_number}: Unmatched parenthesis')


                if statement[index+1] != "(":
                    self.abort(f'Error in line {self.line_number}: Expected "(" got "{statement[index+1]}"')
                else:

                    pairs=0
                    recursive_operation = []
                    n_buffer = index+2
                    index_buffer = 0
                    for command in statement[index+2:]:
                        
                        
                        
                        if command == ")" and pairs == 0:

                            for i in statement[n_buffer:]:
                                if i.isnumeric() or i in self.variables or i in self.operations:
                                    done=False
                                    break
                                else:
                                    done=True
                            break

                        elif command == "(":
                            pairs+=1
                            recursive_operation.append(command)
                        elif command == ")" and pairs != 0:
                            pairs-=1
                            recursive_operation.append(command)
                        elif command != ",":
                            recursive_operation.append(command) 

                        n_buffer+=1
                        index_buffer+=1
                    

                    if operation in self.variables:
                        operations = self.recursive_function(self.variables[operation], recursive_operation)
                    else:
                        operations = self.recursive_function(operation,recursive_operation)
                    
                    commands.append(operations)
            if done == True :
                break

            index+=1
        return commands



    # Returns a list of woodpecker operations that the recursive function corresponds to
    def recursive_function(self, n, statement):

        #print("RECURSIVE FUNCTION")
        output = []

        # Checks for nested recursive operations
        done = False
        index=0
        n_buffer = -1
        for command in statement:


            if command in self.operations and index>n_buffer:
                output.append(command)    
            elif command in self.functions and index>n_buffer:
                output.append(self.functions[command])


            elif command.isnumeric() or command in self.variables:
                if statement[index+1] != "(":
                    self.abort(f'Error in line {self.line_number}: Expected "(" got "{command}"')

                pairs=0
                recursive_operation = []
                n_buffer = index+2
                for operation in statement[index+2:]:                        
                        
                    if operation == ")" and pairs == 0:
                        #print("End of recursive operation")
                        done=True
                        break

                    elif operation == "(":
                        pairs+=1
                        recursive_operation.append(operation)
                    elif operation == ")" and pairs != 0:
                        pairs-=1
                        recursive_operation.append(operation)
                    elif operation != ",":
                        recursive_operation.append(operation) 

                    n_buffer+=1



                test = rparse(self.functions, self.variables)
                output.append(test.recursive_function(command, recursive_operation))

            
            if done==True:
                break

            index+=1
        
        

        return output * int(n)

        
        

    def expression(self, expression):
        #print("EXPRESSION")
        index = 0
        C = 0
        while len(expression) != 1:
            token = expression[index]
            variables = list(self.variables.keys())

            if token == "+":
                if expression[index+1].isnumeric() == False:
                    if expression[index + 1] in variables == False:
                        self.abort(f'Error in line {self.line_number}: Variable "{expression[index+1]}" referenced before assignment')
                    
           
                    A = int(self.variables[expression[index + 1]])
                else:
                    A = int(expression[index + 1])

                if expression[index-1].isnumeric() == False:
                    if expression[index - 1] in variables == False:
                        
                        self.abort(f'Error in line {self.line_number}: Variable "{expression[index-1]}" referenced before assignment')
                    B = int(self.variables[expression[index - 1]])
                else:
                    B = int(expression[index-1])

                C=A+B
                expression.pop(0)
                expression.pop(0)
                expression.pop(0)
                expression.insert(0, str(C))
                index=0
            elif token == "-":
                if expression[index+1].isnumeric() == False:
                    if expression[index + 1] in variables == False:
                        self.abort(f'Error in line {self.line_number}: Variable "{expression[index+1]}" referenced before assignment')
                    
           
                    A = int(self.variables[expression[index + 1]])
                else:
                    A = int(expression[index + 1])

                if expression[index-1].isnumeric() == False:
                    if expression[index - 1] in variables == False:
                        
                        self.abort(f'Error in line {self.line_number}: Variable "{expression[index-1]}" referenced before assignment')
                    B = int(self.variables[expression[index - 1]])
                else:
                    B = int(expression[index-1])

                C=B-A
                expression.pop(0)
                expression.pop(0)
                expression.pop(0)
                expression.insert(0, str(C))
                index=0


            index+=1

        return C
                
                    




    def emit(self):
        return self.emitted_code


    def abort(self, error):
        print(f'Buzz: {error}')
        exit()