"""
8. Dado um número inteiro 𝑛 (𝑛 > 0), seguido de 𝑛 números inteiros, exibir a soma dos 𝑛 números lidos (o
número 𝑛 não entra na soma).
"""
n = int(input("Digite n sendo n>0: "))
acumulador = 0
for cont in range (1, n+1):
    num = int(input("Digite um número a ser somado: "))
    acumulador += num
print("A soma é %d" % acumulador)

#agr com while#

n = int(input("Digite n sendo n>0: "))
acumulador = 0
contador = 1
while contador <= n:
    num = int(input("Digite um número a ser somado: "))
    contador += 1
    acumulador += num
print("A soma é" % acumulador)