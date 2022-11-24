import argparse
from CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from CYK import cyk
from lexer import createToken

def welcome():
    print("\033c", end="")
    print('''
Welcome To 
 _______ _    _    __     _______    _      _______    ______   ________ _______     
|  ___  | |  | |  /  |   |_   __ \  / \    |_   __ \ .' ____ \ |_   __  |_   __ \    
|_/  / /| |__| |_ `| |     | |__) |/ _ \     | |__) || (___ \_|  | |_ \_| | |__) |   
    / / |____   _| | |     |  ___// ___ \    |  __ /  _.____`.   |  _| _  |  __ /    
   / /      _| |_ _| |_   _| |_ _/ /   \ \_ _| |  \ \| \____) | _| |__/ |_| |  \ \_  
  /_/      |_____|_____| |_____|____| |____|____| |___\______.'|________|____| |___| 
                                                                                                           
Ready to Parse your JavaScript Program!
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