"""
6. Dado um número inteiro 𝑛 (𝑛 > 1), exibir os números de 𝑛 − 1 até 1. Quantos serão impressos?
"""
n = int(input("Digite n sendo n>1: "))
cont = n-1
while cont>=1:
    print(cont)
    cont-=1

#será exibido "n-1" valores

n = int(input("Digite n sendo n>1: "))
cont = n-1

for cont in range(cont, 0, -1):
    print(cont)
