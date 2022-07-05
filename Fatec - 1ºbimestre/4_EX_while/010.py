#[EXERCÍCIO 6] Crie um programa que receba valores reais e ao final exiba a
#média aritmética simples dos valores lidos. Observação: o valor 0.0 encerra
#as entradas e não deve ser contabilizado.

acumulador = 0
contador = 0
x = float(input('valor: '))
while x != 0.0:
    acumulador += x
    contador += 1
    x = float(input('valor: '))
print('Média: %.2f' % (acumulador/contador))
