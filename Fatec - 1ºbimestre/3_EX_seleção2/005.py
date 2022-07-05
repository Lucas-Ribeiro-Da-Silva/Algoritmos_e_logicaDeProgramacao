#[EXERCÍCIO 3] Crie um programa que receba três inteiros a, b e x, onde a e b são os
#limites inferior e superior de um intervalo de inteiros, respectivamente, com a < b. O
#programa exibirá uma mensagem indicando se x está no intervalo [a..b] e, caso
#esteja, indicar se x está mais próximo de a ou de b (adote que jamais dará empate).

a = int(input('a: '))
b = int(input('b: '))
x = int(input('x: '))
if a<=x<=b:
    print('Dentro do intervalo')
    if x-a < b-x:
        print(x, 'está mais próximo de', a)
    else:
        print(x, 'está mais próximo de', b)
else:
    print('Fora do intervalo')

