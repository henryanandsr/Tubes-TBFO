import os
import sys
import re

def lex(text, token_rules):
    pos = 0
    current_pos = 1
    line = 1
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            current_pos = 1

        flag = None
        for current_token in token_rules:
            pattern, tag = current_token

            regex = re.compile(pattern)
            flag = regex.match(text,pos)

            if flag:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print(f'\nSYNTAX ERROR\nIllegal char {text[pos]} at line {line} and column {current_pos}')
            sys.exit(1)
        else:
            pos = flag.end(0)
        current_pos += 1

    return tokens

token_rules = [
    
]