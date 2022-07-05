#2. Fornecidos dois números inteiros 𝑎 e 𝑏 (𝑎 > 0 e 𝑏 > 0), verificar se 𝑎 é divisível por 𝑏. Exibir a
#mensagem 'divisível' ou 'não divisível', conforme o caso. Não use o operador de resto.

a = int(input("Digite um número >0: "))
b = int(input("Digite um número >0: "))

#Resto = Dividendo - Divisor*quociente
Q = a//b
R = a - b*Q
print(R)

if R == 0:
    print('divisivel')
else:
    print('não divisivel')