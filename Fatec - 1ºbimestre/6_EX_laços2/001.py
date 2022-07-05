"""
1. Dizemos que um número natural 𝑛 (𝑛 > 0) é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 210 é um número triangular, pois 5 × 6 × 7 = 210.
Fornecido um número natural 𝑛 (𝑛 > 0), exibir 'triangular' ou 'não triangular', conforme o caso.
"""

###for#############
n = int(input("Digite n:"))

for i in range (n):
    triangular = i * (i + 1) * (i+ 2)
    if triangular == n:
        print("triangular")
        break
else:
    print("não triangular")
"""

#####while####################
n = int(input("Digite n:"))
cont = 1

while cont<=n:
    triangular = cont * (cont+1) * (cont+2)
    if triangular  == n:
        print("triangular")
        break
    cont += 1
else:
    print("não triangular")