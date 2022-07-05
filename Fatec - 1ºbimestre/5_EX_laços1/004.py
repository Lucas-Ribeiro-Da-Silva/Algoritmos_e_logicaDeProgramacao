"""
4. Dado um número inteiro 𝑛 (𝑛 > 1), exibir os números múltiplos de 3, até no máximo 𝑛.
"""
n = int(input("Digite n sendo n>1: "))
for i in range(0,n+1,3):
    print(i)

#com while

n = int(input("Digite n sendo n>1: "))
cont = 0
result = cont * 3

while result<=n:
    print(result)
    cont += 1
    result = cont * 3