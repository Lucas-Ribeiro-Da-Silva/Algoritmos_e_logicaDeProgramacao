# 4. Fornecidos três números reais distintos 𝑎, 𝑏 e 𝑐, exibir o maior valor. (seleção encadeada)

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

if a>b and a>c:
    print(a)
elif b>c:
    print (b)
else:
    print('o maior número é', c)