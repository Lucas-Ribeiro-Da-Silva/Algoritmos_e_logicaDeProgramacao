#[EXEMPLO 2] Crie um programa que receba apenas letras maiúsculas e minúsculas e
#exiba a quantidade de letras lidas. Observação: as leituras serão encerradas quando
#a letra maiúscula 'F' for inserida (não deve ser contabilizada).

contador = 0
L = input('Letra: ')
while L != 'F':
    contador += 1
    L = input('Letra: ')
print('Letras informadas: %d' % contador)
