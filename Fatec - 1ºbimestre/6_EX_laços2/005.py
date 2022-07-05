"""
5. Fornecido um número inteiro 𝑛 (𝑛 > 0), exibir os dígitos de 𝑛 em ordem inversa (use // e %).
Exemplo: Entrada: 4690 → Saída: 0964
"""

n = int(input("n?"))
while n>0:
    x = n%10
    print(x, end='')
    n = n//10



