import argparse
from CFGtoCNF import*
from CYK import*
from lexer import*
from time import *

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

    start = time()
    token = createToken(args.file.name)
    token = [x.lower() for x in token]
    CNFgrammar = CNFMap(CFGConverter((readCFG("CFG.txt"))))
    # print("Your code is: ")
    # print(token)
    # print()
    # print("Result :")
    cyk(token, CNFgrammar)
    end = time()
    print("Parsing Time: " + str(round(end-start,2)) + " seconds")

if __name__ == "__main__":
    verdict()