#[EXEMPLO 4] Crie um programa que receba valores reais e ao final exiba a
#soma dos valores lidos. Observação: o valor 99.99 encerra as entradas e não
#deve ser contabilizado.

acumulador = 0.0
x = float(input('valor: '))
while x != 99.99:
    acumulador += x
    x = float(input('valor: '))
print('Soma: %.2f' % acumulador)
