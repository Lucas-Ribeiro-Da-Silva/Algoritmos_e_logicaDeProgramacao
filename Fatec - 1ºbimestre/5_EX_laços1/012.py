"""
12. Dados números reais, exibir a média aritmética deles. A entrada termina com a leitura do número zero.
"""

acumulador = 0
qtd = 0
while True:
    n = float(input("n?"))
    if n == 0:
        break
    acumulador += n
    qtd += 1
print(acumulador / qtd)

