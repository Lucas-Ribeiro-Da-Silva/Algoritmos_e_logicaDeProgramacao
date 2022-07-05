"""
17. Dados dois números inteiros 𝑝 (𝑝 ≥ 0) e 𝑞 (𝑞 > 0), exibir a divisão inteira de 𝑝 por 𝑞 sem usar os
operadores de divisão, multiplicação e/ou potência
"""
p = int(input("p=dividendo: "))
q = int(input("q=divisor: "))
cont = 0

while q <= p:
    p-=q
    cont += 1
print(cont)

############ ou ################


p = int(input("p=dividendo: "))
q = int(input("q=divisor: "))
num = 0

while p>0:
    num += 1
    p-=q
print(num)

