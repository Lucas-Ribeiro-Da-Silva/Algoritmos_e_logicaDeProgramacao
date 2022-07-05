#[EXEMPLO 4] Crie um programa que receba dois números inteiros x e y e um
#caractere op representando um operador aritmético (+, -, * ou /). O programa
#deverá exibir o inteiro resultante da expressão x op y.

x = int(input('x: '))
op = input('operador: ')
y = int(input('y: '))
if op == '+':
    print('%d %s %d = %d' % (x, op, y, x+y))
else:
    if op == '-':
        print('%d %s %d = %d' % (x, op, y, x-y))
    else:
        if op == '*':
            print('%d %s %d = %d' % (x, op, y, x*y))
        else:
            print('%d %s %d = %d' % (x, op, y, x/y))

#ou................................................................

x = int(input('x: '))
op = input('operador: ')
y = int(input('y: '))
if op == '+':
    print('%d %s %d = %d' % (x, op, y, x+y))
elif op == '-':
    print('%d %s %d = %d' % (x, op, y, x-y))
elif op == '*':
    print('%d %s %d = %d' % (x, op, y, x*y))
else:
    print('%d %s %d = %d' % (x, op, y, x/y))