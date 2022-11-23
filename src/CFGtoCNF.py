import keyword
terminal = keyword.kwlist
ruleDict = {}

# Grammar Reader
def grammarReadFile(file):
    with open(file) as cfg:
        row = cfg.readline()
        row_converted = []
        for i in range (len(row)):
            splitRow = row[i].replace("->","").split()
            row_converted.append(splitRow)
    return row_converted

# Grammar Output
def grammarOutputFile(grammar):
    for rules in grammar:
        for i in range(len(rules)):
            if i == 0:
                print(rules[i], " -> ", end="")
            else:
                print(rules[i], end=" ")
        print("\n")

# Add to dictionary
def addToDictionary(rule):
    global ruleDict
    if rule[0] not in ruleDict:
        ruleDict[rule[0]] = []
    ruleDict[rule[0]].append(rule[1:])

# Convert to CNF
def cfgToCNF(grammar):
    global ruleDict
    idx = 0
    unit_production = []
    result = []

    for rule in grammar:
        new_rule = []
        # Untuk yang miliki 1 nonterminal / terminal di kanan
        if len(rule) == 2 and not rule[1][0].islower():
            unit_production.append(rule)
            addToDictionary(rule)
            continue

        # Untuk yang miliki lebih dari 3 nonterminal, akan diubah menjadi 3 saja
        while len(rule) > 3:
            new_rule.append([f"{rule[0]}{idx}", rule[1], rule[1], rule[2]])
            rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
            idx += 1
        
        if rule:
            addToDictionary(rule)
            result.append(rule)
        
        if new_rule:
            for i in range(len(new_rule)):
                result.append(new_rule[i])
        
    while unit_production:
        rule = unit_production.pop()
        if rule[1] in ruleDict:
            for item in ruleDict:
                new_rule = [rule[0]] + item

                # Nonterminal di kanan bakal diubah panjangnya menjadi 3
                if len(new_rule) > 2 or new_rule[1][0].islower():
                    result.append(new_rule)

                # Jika hanya memiliki 2 nonterminal, akan ditambahkan ke unit production
                else:
                    unit_production.append(new_rule)
                addToDictionary(new_rule)
    return result

def grammarMapping(grammar):
    grammar_length = len(grammar)
    map = {}
    for rule in grammar:
        map[str(rule[0])] = []
    for rule in grammar:
        element = []
        for i in range(1, len(rule)):
            insert = rule[i]
            element.append(insert)
        map[str(rule[0])].append(element)
    return map

def grammarWriter(grammar):
    file = open("CNF.txt", "w")
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

if __name__ = "__main__":
    grammarWriter(cfgToCNF(grammarReadFile("CFG.txt")))