"""
6. Fornecido um número inteiro 𝑛 (𝑛 > 10), determine se os dígitos de 𝑛 estão em ordem estritamente
crescente. Exibir 'sim' ou 'não', conforme o caso (use // e %).
Exemplos: Entrada: 577 → Saída: 'não'
Entrada: 2579 → Saída: 'sim'
"""


n = int(input('n: '))
x1 = n
while n > 0:
    resto = n % 10
    n = n // 10
    if resto <= x1:
        x1 = resto
        if n<=0:
            print('sim')
    else:
        print('não')
        break
