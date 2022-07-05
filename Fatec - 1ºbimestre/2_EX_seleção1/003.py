#3. Fornecido um número 𝑛 e um intervalo fechado de 𝑎 até 𝑏 (𝑎 < 𝑏),
# verificar se 𝑛 está no intervalo.
# Exibir a mensagem 'no intervalo' ou 'fora do intervalo', conforme o caso.

n = int(input("Digite um numero:"))
a = int(input("Digite numero 'A':"))
b = int(input("Digite numero 'B':"))
if n >= a and n <= b:
    print("no intervalo")
else:
    print("fora do intervalo")
