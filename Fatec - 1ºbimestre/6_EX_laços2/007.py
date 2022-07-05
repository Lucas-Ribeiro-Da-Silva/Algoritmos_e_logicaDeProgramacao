"""
7. Fornecido um número inteiro 𝑛 (𝑛 > 1), verifique se 𝑛 é um número primo. Exibir 'primo' ou 'não primo',
conforme o caso.
"""

n = int(input("n?"))
cont = 0
for i in range(1, n +1):
    if n % i == 0:
        cont += 1
if cont == 2:
    print('primo')
else:
    print('não primo')
