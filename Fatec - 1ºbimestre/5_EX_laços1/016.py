"""
16. Dado um número inteiro 𝑛 (𝑛 > 0), seguido de 𝑛 números inteiros, exibir o menor número lido.
"""

####while#####
"""
n = int(input("n?"))
cont = 0
x = n
while cont < x:
    num = int(input("num?"))
    if num<n:
        n = num
    cont+=1
print(n)
"""


#### for ####
n = int(input("n?"))
num = n
for i in range (n):
    numero = int(input("n?"))
    if numero < num:
        num = numero
print(num)

