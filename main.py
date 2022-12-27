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

        parsed_program = parse(program_tokens)

        emit = emitter(parsed_program.emit(), args.output_filename)
        emit.emit_code()

        print(f'Successfully compiled {args.filename} into {args.output_filename}!')        

if __name__=="__main__":
    main()