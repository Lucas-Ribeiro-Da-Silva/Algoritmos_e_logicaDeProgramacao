"""
7. Dado um número inteiro 𝑛 (𝑛 > 0), exibir os 𝑛 primeiros pares, iniciando em trinta.
"""
n = int(input("Digite n sendo n>0: "))
for i in range(30, (30+ 2*n) , 2):
    print(i)
