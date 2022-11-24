import argparse
from CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from CYK import cyk
from lexer import createToken

def welcome():
    print("\033c", end="")
    print('''
Welcome To 
 _______ _    _    __       ______                            _  __                 
|  ___  | |  | |  /  |    .' ___  |                          (_)[  |                
|_/  / /| |__| |_ `| |   / .'   \_| .--.  _ .--..--. _ .--.  __  | | .---.  _ .--.  
    / / |____   _| | |   | |      / .'`\ [ `.-. .-. [ '/'`\ [  | | |/ /__\\[ `/'`\] 
   / /      _| |_ _| |_  \ `.___.'\ \__. || | | | | || \__/ || | | || \__., | |     
  /_/      |_____|_____|  `.____ .''.__.'[___||__||__] ;.__/[___|___]'.__.'[___]    
                                                    [__|                                          
Ready to Parse your Arse!
        ''')

def verdict():
    arg = argparse.ArgumentParser()
    arg.add_argument('file', type = argparse.FileType('r'))
    args = arg.parse_args()

    welcome()
    print("File name: " + str(args.file.name))
    print()

    token = createToken(args.file.name)
    token = [x.lower() for x in token]
    CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("CFG.txt"))))
    # print("Your code is: ")
    # print(token)
    # print()
    # print("Result :")
    cyk(token, CNFgrammar)

if __name__ == "__main__":
    verdict()