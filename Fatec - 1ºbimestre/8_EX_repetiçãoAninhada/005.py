"""
[EXTRA 1] Crie um programa que exiba 5 linhas com 3 colunas, como se fosse uma matriz
em que os itens são a soma de suas próprias coordenadas (linha,coluna).
"""

for i in range(5):
    for j in range(3):
        print('(%d+%d=%d) ' % (i,j,i+j), end='')
    print()


"""
[EXTRA 2] Crie um programa que leia um natural n e exiba os fatoriais dos n
primeiros naturais.
"""

n = int(input('n: '))
for x in range(n):
    f = 1
    for i in range(1, x+1):
        f = f * i
    print('%d! = %d' % (x, f))
    
    
"""
[EXTRA 3] Crie um programa que leia um natural n e exiba os termiais dos n
primeiros naturais.
"""

n = int(input('n: '))
for x in range(n):
    t = 0
    for i in range(1, x+1):
        t = t + i
    print('%d? = %d' % (x, t))

"""
[EXTRA 4] Crie um programa que leia dois naturais p e u (1<p≤u) e exiba
todos os números primos do intervalo [p..u].
"""

p = int(input('p: '))
u = int(input('u: '))
for n in range(p, u+1):
    qtd = 0
    for d in range(1, n+1):
        if n%d == 0:
            qtd += 1
    if qtd==2:
        print(n, end=' ')

"""
[EXTRA 5] Crie um programa para um site de compras que solicita aos clientes seus créditos
e verifica, a cada item comprado, se há crédito suficiente para incluir o item no carrinho. A
compra de cada cliente será finalizada quando inserido um item com valor zero.
"""

while True:
    credito = float(input('Crédito: '))
    carrinho = 0.0
    item = float(input('Item: '))
    while item != 0.0:
        if carrinho+item > credito:
            print('Crédito insuficiente')
        else:
            carrinho += item
        item = float(input('Item: '))
    print('Carrinho: R$ %.2f' % carrinho)
    clientes = input('\nHá mais clientes? ')
    if clientes=='N': break
