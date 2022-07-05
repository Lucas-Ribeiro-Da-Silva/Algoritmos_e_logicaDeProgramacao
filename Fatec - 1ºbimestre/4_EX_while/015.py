#[EXERCÍCIO 8] Crie um programa que receba um número inteiro n e, caso n seja um número natural, exiba uma mensagem
# indicando se n é par ou ímpar. Enquanto n for um número negativo, repita a solicitação de entrada.

while True:
    n = int(input('n: '))
    if n>=0: break
if n%2==0:
    print('par')
else:
    print('ímpar')
