import argparse
from CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from CYK import cyk
from lexer import createToken

def welcome():
    print()
    print("Welcome to the CFG to CNF converter and CYK parser!")

def verdict():
    arg = argparse.ArgumentParser()
    arg.add_argument('file', type = argparse.FileType('r'))
    args = arg.parse_args()

    welcome()
    print("\nLoading...")
    print("Checking your codes...")
    print("File name: " + str(args.file.name))
    print()

    token = createToken(args.file.name)
    token = [x.lower() for x in token]
    CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("CFG.txt"))))
    print("Your code is: ")
    cyk(token, CNFgrammar)

if __name__ == "__main__":
    verdict()