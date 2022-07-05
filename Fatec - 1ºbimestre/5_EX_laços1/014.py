"""
14. Dadas letras, uma por linha, exibir a quantidade de vogais lidas. A entrada é finalizada pelo caractere '!'.
"""

acumulador = 0
while True:
    letra = input("Digite uma letra: ")
    if letra == "!":
        break
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        acumulador += 1
print(acumulador)