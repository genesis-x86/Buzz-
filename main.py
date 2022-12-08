import argparse
from Lexer.lexer import lexer

def main():
        
    parser = argparse.ArgumentParser(description="Buzz! programming language parser for Woodpecker CPU")
    parser.add_argument('filename')
    args = parser.parse_args()

    with open(args.filename) as file:
        test = lexer(file)

if __name__=="__main__":
    main()