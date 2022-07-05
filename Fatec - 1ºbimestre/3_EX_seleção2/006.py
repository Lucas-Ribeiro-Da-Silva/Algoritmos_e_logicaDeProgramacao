#[EXEMPLO 3] Crie um programa que receba dois reais x e y e exiba uma mensagem
#indicando se x é menor que y, ou se x é maior que y ou se ambos são iguais.

x = float(input('x:'))
y = float(input('y:'))

if x<y:
    print('%.2f é menor que %.2f' % (x, y))
elif x>y:
    print('%.2f é menor que %.2f' % (x, y))
else:
    print('%.2f é igual a %.2f' % (x, y))

# ambas as formas corretas


x = float(input('x: '))
y = float(input('y: '))
if x < y:
    print('%.2f é menor que %.2f' % (x, y))
else:
    if x > y:
        print('%.2f é maior que %.2f' % (x, y))
    else:
        print('%.2f é igual a %.2f' % (x, y))

#ou....................................................

x = float(input('x: '))
y = float(input('y: '))
if x < y:
    print('%.2f é menor que %.2f' % (x, y))
elif x > y:
    print('%.2f é maior que %.2f' % (x, y))
else:
    print('%.2f é igual a %.2f' % (x, y))