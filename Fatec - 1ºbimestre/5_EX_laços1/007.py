"""
7. Dado um nรบmero inteiro ๐ (๐ > 0), exibir os ๐ primeiros pares, iniciando em trinta.
"""
n = int(input("Digite n sendo n>0: "))
for i in range(30, (30+ 2*n) , 2):
    print(i)
