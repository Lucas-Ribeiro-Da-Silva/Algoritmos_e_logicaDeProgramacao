def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def preenche(v, n):
    for i in range(n):
        v[i] = int(input('v[%d]? ' % i))

v1 = 4*[0]
exibe(v1, 4)
preenche(v1, 4)
exibe(v1, 4)

