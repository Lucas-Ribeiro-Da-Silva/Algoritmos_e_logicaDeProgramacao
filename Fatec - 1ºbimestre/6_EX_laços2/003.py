"""
3. Fornecidas letras maiúsculas, lidas uma por vez, até ocorrer uma fora de ordem, exibir a quantidade de
letras lidas, exceto a letra fora de ordem. Exemplo: 'A', 'C', 'K', 'M', 'M', 'T', 'B' → 6.
"""

letra = input("letra?")
contadora = 0
acumuladora = letra

while letra >= acumuladora:
    acumuladora = letra
    contadora += 1
    letra = input("letra?")
print(contadora)
