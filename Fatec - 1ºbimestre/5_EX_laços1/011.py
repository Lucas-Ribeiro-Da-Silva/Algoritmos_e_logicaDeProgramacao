"""
11. Dados números inteiros, exibir a soma deles. A entrada termina com a leitura do número zero. Ao menos
um número será lido antes do zero.
"""

acumulador = 0
while True:
    n = int(input("n?"))
    if n == 0 and acumulador > 0:
        break
    acumulador += n
print(acumulador)