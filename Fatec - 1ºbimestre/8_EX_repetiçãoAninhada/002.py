"""
[EXEMPLO 6] Altere o programa do Exemplo 5 de modo que a cada 24 horas
os três mostradores sejam zerados e o relógio reinicie a contagem.
"""
from time import sleep
    while True:
        h = 0
        while h < 24:
            m = 0
            while m < 60:
                s = 0
                while s < 60:
                    print('%02d:%02d:%02d' % (h, m, s))
                    s += 1
                    sleep(1)
                m += 1
            h += 1



from time import sleep
while True:
    for h in range(24):
        for m in range(60):
            for s in range(60):
                print('%02d:%02d:%02d' % (h, m, s))
                sleep(1)



"""
[EXEMPLO 7] Altere o programa do Exemplo 6 de modo que o mostrador
inicie em 23:59:59 e a contagem de tempo seja decrescente.
"""

from time import sleep
while True:
    h = 23
    while h >= 0:
        m = 59
        while m >= 0:
            s = 59
            while s >= 0:
                print('%02d:%02d:%02d' % (h, m, s))
                s -= 1
                sleep(1)
            m -= 1
        h -= 1


from time import sleep
while True:
    for h in range(23, -1, -1):
        for m in range(59, -1, -1):
            for s in range(59, -1, -1):
                print('%02d:%02d:%02d' % (h, m, s))
                sleep(1)


"""
[EXEMPLO 8] Crie um programa que exiba 2 linhas com 4 colunas do caractere '*'.
"""

for i in range(2):
    for j in range(4):
        print('*', end='')
    print()

