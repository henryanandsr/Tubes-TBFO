import sys

def cyk(token,grammar):
    animation = "|/-\\"
    # Membuat tabel dengan ukuran token
    tab = [[set() for i in range(len(token))] for j in range(len(token))]
    for i in range(len(token)): # Iterasi untuk setiap token
        for key in grammar: # Iterasi untuk setiap key pada grammar
            for rule in grammar[key]: # Iterasi untuk setiap rule pada grammar
                if len(rule) == 1 and rule[0] == token[i]: # Jika rule hanya memiliki 1 token dan sama dengan token
                    tab[i][i].add(key)
                    sys.stdout.write("\rLoading..." + animation[i % len(animation)])

     # Iterasi kedua untuk setiap token
    for j in range(len(token)):
        for i in range(j,-1,-1): 
            for k in range(i,j):
                for key in grammar:
                    for rule in grammar[key]:
                        # Jika rule memiliki 2 token dan token pertama ada di tab[i][k] dan token kedua ada di tab[k+1][j]
                        if len(rule) == 2 and rule[0] in tab[i][k] and rule[1] in tab[k+1][j]:
                            tab[i][j].add(key)
            sys.stdout.write("\rLoading..." + animation[i % len(animation)])
            
    print()
    if 'S' in tab[0][len(token)-1]:
        print("Program Successfully Compiled!!! ^V^")
    else:
        print("Program Failed to Compile T_T")

if __name__ == "__main__":
    pass