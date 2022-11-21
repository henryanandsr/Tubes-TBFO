def grammar_to_arr(filename):
    grammar = []
    file = open(f'{filename}')
    for line in file:
        grammar.append(line.split())
    return grammar