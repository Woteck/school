G = {}
G['a'] = ['b', 'c']
G['b'] = ['a', 'd', 'e']
G['c'] = ['a', 'd']
G['d'] = ['b', 'c', 'e']
G['e'] = ['b', 'd', 'f', 'g']
G['f'] = ['e', 'g']
G['g'] = ['e', 'f', 'h']
G['h'] = ['g']

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = len(liste)
A = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if liste[j] in G[liste[i]]:
            A[i][j] = 1

for i in range(n):
    print(A[i])