rules_dictionary = {}

# Read CFG From txt File
def readCFG(filename):
    with open(filename) as cfg:
        row = cfg.readlines()
        read_result = []
        for i in range (len(row)):
            row_split = row[i].replace("->","").split()
            read_result.append(row_split)
    return read_result

# Function to add rule to rules
def addRule(rule):
    global rules_dictionary
    if rule[0] not in rules_dictionary:
        rules_dictionary[rule[0]] = []
    rules_dictionary[rule[0]].append(rule[1:])

# Function to convert CFG to CNF
def CFGConverter(grammar):
    global rules_dictionary
    index = 0
    unit_rules = []
    result = []
    for rule in grammar:
        new_rule = []
        # Untuk grammar yang memilki satu nonterminal/terminal
        if len(rule) == 2 and not rule[1][0].islower():
            unit_rules.append(rule)
            addRule(rule)
            continue
        # Proses Split untuk grammar yang memiliki lebih dari 3 nonterminal/terminal
        while len(rule) > 3:
            new_rule.append([f"{rule[0]}{index}", rule[1], rule[2]])
            rule = [rule[0]] + [f"{rule[0]}{index}"] + rule[3:]
            index += 1
        
        if rule:
            addRule(rule)
            result.append(rule)
        
        if new_rule:
            for i in range(len(new_rule)):
                result.append(new_rule[i])

    # Algoritma untuk yang hanya memiliki 1 nonterminal di bagian kanan
    while unit_rules:
        rule = unit_rules.pop()
        if rule[1] in rules_dictionary:
            for i in rules_dictionary[rule[1]]:
                new_rule = [rule[0]] + i
                # Nonterminal di bagian kanan akan diubah kalau panjangnya lebih dari 2 atau memiliki terminal
                if len(new_rule) > 2 or new_rule[1][0].islower():
                    result.append(new_rule)
                else:
                    unit_rules.append(new_rule)
                addRule(new_rule)

    return result

# Membuat map untuk grammar yang sudah diubah
def CNFMap(grammar):
    map = {}
    for rule in grammar:
        map[str(rule[0])] = []

    for rule in grammar:
        element = []
        for i in range(1, len(rule)):
            element.append(rule[i])
        map[str(rule[0])].append(element)

    return map

# Convert CNF to TXT
def CNFWriter(grammar):
    file = open('cnf_new.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

if __name__ == "__main__":
  CNFWriter(CFGConverter((readCFG("CFG.txt")))) 