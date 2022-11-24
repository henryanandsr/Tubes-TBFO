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
            print("SYNTAX ERROR !!!")
            print(f'Error Expression at line {line}: {text[pos:].splitlines()[0]}')
            sys.exit(1)
        else:
            pos = flag.end(0)
        current_pos += 1

    return tokens

token_rules = [

    # Not Token
    (r'[ \t]+', None),
    (r'//.*', None),
    (r'/\*(.|\n)*?\*/', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # OPERATOR
    (r'===', 'EQUAL_OPERATOR'),
    (r'==', 'EQUAL_TO_OPERATOR'),
    (r'!==', 'NOT_EQUAL_OPERATOR'),
    (r'!=', 'NOT_EQUAL_TO_OPERATOR'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'!', 'NOT'),
    (r'\+=', 'SUMPLUS'),
    (r'\-=', 'SUMMIN'),
    (r'\/=', 'SUMDIV'),
    (r'\*=', 'SUMMULT'),
    (r'<=', 'LEQ'),
    (r'<', 'LE'),
    (r'>=', 'GEQ'),
    (r'>', 'GE'),
    (r'=', 'ASSIGN'),
    (r'%', 'MODULO'),
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
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\/', 'DIV'),
    (r'\*', 'MULT'),
    (r'\.', 'DOT'),
    
    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'\bconst\b',              "VAR"),
    (r'\bvar\b',                "VAR"),

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
    (r'\bfunction\b', 'FUNC'),
    (r'\bbreak\b', 'BREAK'),
    (r'\bthrow\b', 'THROW'),
    (r'\bnew\b', 'NEW'),
    (r'\bcontinue\b', 'CONTINUE'),
    (r'\bclass\b', 'CLASS'),

    # Untuk Variabel
    (r'[A-Za-z_][A-Za-z0-9_]*', 'VAR'),
]

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters, token_rules)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)

    # Write file
    # path = os.getcwd()
    # fileWrite = open(path + "./tokenResult.txt", 'w')
    # for token in tokenResult:
    #     fileWrite.write(str(token)+" ")
        # print(token)
    # fileWrite.close()

    return tokenResult