#[EXEMPLO 3] Crie um programa que receba um natural n seguido de n letras minúsculas e exiba,
# ao final, a quantidade de vogais lidas.

n = int(input('Quantidade: '))
vogais = 0
contador = 0
while contador < n:
    L = input('Letra: ')
    if L=='a' or L=='e' or L=='i' or L=='o' or L=='u':
        vogais += 1
    contador += 1
print('Vogais: %d' % vogais)
