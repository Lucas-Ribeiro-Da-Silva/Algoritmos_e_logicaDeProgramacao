#3. Fornecido um nรบmero ๐ e um intervalo fechado de ๐ atรฉ ๐ (๐ < ๐),
# verificar se ๐ estรก no intervalo.
# Exibir a mensagem 'no intervalo' ou 'fora do intervalo', conforme o caso.

n = int(input("Digite um numero:"))
a = int(input("Digite numero 'A':"))
b = int(input("Digite numero 'B':"))
if n >= a and n <= b:
    print("no intervalo")
else:
    print("fora do intervalo")
