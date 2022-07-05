# 3. Fornecido um número inteiro 𝑛 (𝑛 > 10),
# exibir o valor correspondente aos dois dígitos mais à direita de 𝑛,
# sem utilizar o operador de resto.

num = int(input("Digite um número maior que 10: "))
#Resto = Dividendo - Divisor*quociente
Q = num//100
R = num - 100*Q
print(R)
