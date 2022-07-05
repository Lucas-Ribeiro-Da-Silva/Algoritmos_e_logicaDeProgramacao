def exibe(v, n, rotulo):
    print(rotulo, '=', end=' ')
    for i in range(n):
        print(v[i], end=' ')
    print()

def preenche(v, n, rotulo):
    for i in range(n):
        v[i] = int(input('%s[%d]? ' % (rotulo, i)))

def soma_vetores(a, b, c, tam):
    for i in range(tam):
        c[i] = a[i] + b[i]

tam = int(input('Tamanho dos vetores? '))

a = tam*[0]
b = tam*[0]
c = tam*[0]

preenche(a, tam, 'a')
exibe(a, tam, 'a')

preenche(b, tam, 'b')
exibe(b, tam, 'b')

soma_vetores(a, b, c, tam)
exibe(c, tam, 'c')

