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

    # COMMENT
    (r'//.*', None),
    (r'/\*(.|\n)*?\*/', None),

    # KEYWORDS
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\bdo\b', 'DO'),
    (r'\bfor\b', 'FOR'),
    (r'\btrue\b', 'TRUE'),
    (r'\bfalse\b', 'FALSE'),
    (r'\bconst\b', 'CONST'),
    (r'\bint\b', 'INT'),
    (r'\bchar\b', 'CHAR'),
    (r'\blet\b', 'LET'),
    (r'\bfloat\b', 'FLOAT'),
    (r'\bstring\b', 'STRING'),
    (r'\bvar\b', 'VAR'),
    (r'\bswitch\b', 'SWITCH'),
    (r'\bcase\b', 'CASE'),
    (r'\bdefault\b', 'DEFAULT'),
    (r'\btry\b', 'TRY'),
    (r'\bcatch\b', 'CATCH'),
    (r'\breturn\b', 'RETURN'),
    (r'\bfinally\b', 'FINALLY'),

    # OPERATOR
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\/', 'DIV'),
    (r'\*', 'MULT'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'!', 'NOT'),
    (r'\+=', 'SUMPLUS'),
    (r'\-=', 'SUMMIN'),
    (r'<', 'LE'),
    (r'<=', 'LEQ'),
    (r'>=', 'GEQ'),
    (r'>', 'GE'),
    (r'===', 'EQUAL_OPERATOR'),
    (r'!==', 'NOT_EQUAL_OPERATOR'),
    (r'=', 'ASSIGN'),
    (r'%', 'MODULO'),

    # PUNCTUATION
    (r'\,', 'KOMA'),
    (r'\;', 'TITIK_KOMA'),
    (r'\:', 'TITIK_DUA'),
    (r'\{', 'KURUNG_KURAWAL_BUKA'),
    (r'\}', 'KURUNG_KURAWAL_TUTUP'),
    (r'\(', 'KURUNG_BUKA'),
    (r'\)', 'KURUNG_TUTUP'),
    (r'\[', 'OPEN_BRACKET'),
    (r'\]', 'CLOSE_BRACKET'),
    (r'\n', 'ENTER'),
    
]