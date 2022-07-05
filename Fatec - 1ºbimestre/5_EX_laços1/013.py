"""
13. Dadas letras, uma por linha, exibir a quantidade de letras lidas. A entrada é finalizada pelo caractere '!'.
"""

#meu jeito
acumulador = 0
while True:
    letra = input("Digite uma letra: ")
    if letra == "!":
        break
    acumulador += 1
print(acumulador)

#jeito do professor
qtd = 0
L = input('Letra?')
while L != '!':
    qtd += 1
    L = input('Letra?')
print('Quantidade de letra =', qtd)


