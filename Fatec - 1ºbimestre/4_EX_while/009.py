#[EXERCÍCIO 5] Crie um programa que receba valores reais e ao final exiba a
#soma dos valores positivos lidos. Observação: o valor 99.99 encerra as
#entradas e não deve ser contabilizado.

acumulador = 0
x = float(input('valor: '))
while x != 99.99:
    if x > 0:
        acumulador += x
    x = float(input('valor: '))
print('Soma positivos: %.2f' % acumulador)
