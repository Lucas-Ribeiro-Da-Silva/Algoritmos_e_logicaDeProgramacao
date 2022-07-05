# 5. Fornecido um número inteiro 𝑛 (1000 ≤ 𝑛 ≤ 9999),
# exibir a soma dos dois dígitos à esquerda com os dois dígitos à direita.
# Exemplo: 𝑛 = 3689, logo, a saída é 36 + 89 = 125

num = int(input("Digite um número entre 1000 e 9999: "))
x = num // 100
y = num % 100
print(x + y)
