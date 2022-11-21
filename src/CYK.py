def cyk(rule, word):
    n = len(word)
    table = [[set() for i in range(n)] for j in range(n)]

    for i in range(n):
        for r in rule:
            if r[1] == word[i]:
                table[0][i].add(r[0])

    for i in range(1, n):
        for j in range(n - i):
            for k in range(i):
                for r in rule:
                    if r[1] == table[k][j] and r[2] == table[i - k - 1][j + k + 1]:
                        table[i][j].add(r[0])

    return table