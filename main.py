import argparse
from Lexer.lexer import lexer
from Parser.parser import parse
from Emitter.emitter import emitter

        
def main():
        
    parser = argparse.ArgumentParser(description="Buzz! programming language parser for Woodpecker CPU")
    parser.add_argument('filename')
    parser.add_argument('output_filename')
    args = parser.parse_args()

    with open(args.filename) as file:
        program = lexer(file)

        program_tokens, program_types = program.parse_tokens()

        parsed_program = parse(program_tokens, program_types)

        emit = emitter(parsed_program.emit(), args.output_filename)

        print(f'Successfully compiled {args.filename} into {args.output_filename}!')        

        #print(program_types)
        #print(program_tokens)

        #print(f'DEBUG{program_types}')
        #test = buzz_parser()
        #statements, statement_types = test.parse_statements(program_tokens, program_types)
        #test.match(statement_types)


if __name__=="__main__":
    main()