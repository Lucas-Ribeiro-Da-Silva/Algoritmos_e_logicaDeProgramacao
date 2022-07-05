"""
4. Fornecido um número inteiro 𝑛 (𝑛 > 10), exibir 'possui', caso 𝑛 possua pelo menos dois algarismos
adjacentes sendo um ímpar e o outro par, ou 'não possui', caso contrário (use o operador de resto %).
Exemplos: Entrada: 532 → Saída: possui
Entrada: 1357 → Saída: não possui
"""

n = int(input("n?"))
c_par = 0
c_impar = 0
while n>0:
    x = n % 10
    if x % 2 == 0:
        c_par += 1
    else:
        c_impar += 1
    n = n // 10
if c_par > 0 and c_impar > 0:
    print('possui')
else:
    print('não possui')

