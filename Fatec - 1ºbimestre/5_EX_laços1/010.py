"""
10. Dados números inteiros, exibir a soma deles. A entrada termina com a leitura do número zero.
"""

acumulador = 0
while True:
    n = int(input("n?"))
    if n == 0:
        break
    acumulador += n
print(acumulador)