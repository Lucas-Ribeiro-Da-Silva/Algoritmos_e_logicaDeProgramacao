"""
2. Fornecido um número inteiro 𝑛 (𝑛 > 1), exibir os 𝑛 primeiros termos da sequência: 1, 3, 6, 10, 15, …
"""
### while###
"""
n = int(input("Digite n:"))
cont = 0
acumulador = 1
i = 2
while cont < n:
    print(acumulador)
    acumulador += i
    cont += 1
    i += 1
"""

### for ###
n = int(input("Digite n:"))
acumulador = 1
i = 2
for cont in range (n):
    print(acumulador)
    acumulador += i
    i += 1






