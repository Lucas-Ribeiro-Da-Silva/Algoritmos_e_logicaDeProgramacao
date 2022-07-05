#1. Observe as seguintes características:
#O número 2025 tem: 20 + 25 = 45 e 45 × 45 = 2025
#O número 1063 tem: 10 + 63 = 73 e 73 × 73 ≠ 1063
#Dado um número inteiro positivo 𝑛 de quatro dígitos, verificar se 𝑛 é um número cuja raiz quadrada é
#formada pela soma de suas dezenas. Exibir 'sim' ou 'não'. Não use o operador de potência, nem funções.


num = int(input("Digite um número de 4 digitos:"))
x = num //100
y = num % 100
soma = x + y
if soma * soma == num:
    print("sim")
else:
    print("não")