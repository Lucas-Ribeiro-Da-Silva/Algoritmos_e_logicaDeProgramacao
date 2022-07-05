# Crie um programa que receba como entrada os preços de
# diversas mercadorias. O programa deverá somar o preço de
# todas as mercadorias informadas e, ao final, exibir a
# soma, a média de preços e os preços acima dessa média.
# Obs.(1): considere "diversas" como 10.
# Obs.(2): o programa pode conter funções criadas por você.
# Exemplo de uso:
# Entrada:
#    4.0 6.0 10.0 30.0 1.0 50.0 25.0 1.0 1.0 1.0
#    (cada preço está em uma linha diferente)
# Saída:
#    Soma = R$ 129.00
#    Média = R$ 12.90
#    Acima da média:
#                    R$ 30.00
#                    R$ 50.00
#                    R$ 25.00

"""
lista = []
soma = 0
for i in range(10):
    preco = float(input('Preço: '))
    lista.append(preco)
    soma+=preco
media = soma/10

print(f'Soma = R${soma:.2f}')
print(f'Média = R${media:.2f}')
print('Acima da média:')

for item in lista:
    if item>media:
        print(' '*15, 'R$%.2f' % item)
"""

def soma(*args):
    soma = 0
    cont = 0
    lista=[]
    for item in args:
        soma+=item
        cont+=1
        lista.append(item)
    print(f'Soma = R${soma:.2f}')
    return soma, cont, lista

def media(n, d):
    media = n/d
    print(f'Média = R${media:.2f}')
    return media

def acima_media(valor, media):
    for item in valor:
        if item > media:
            print(' ' * 15, 'R$%.2f' % item)


x = soma(4.0, 6.0, 10.0, 30.0, 1.0, 50.0, 25.0, 1.0, 1.0, 1.0)
y = media(x[0], x[1])
acima_media(x[2], y)




