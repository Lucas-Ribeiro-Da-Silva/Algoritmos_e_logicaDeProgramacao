#[EXERCÍCIO 5] Altere o Exemplo 4, de modo que o usuário seja alertado caso tente fazer uma operação de divisão com divisor zero.
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
            if y==0:
                print('Não é possível dividir por zero!')
            else:
                print('%d %s %d = %d' % (x, op, y, x/y))
# ou....................................................................
x = int(input('x: '))
op = input('operador: ')
y = int(input('y: '))
if op == '+':
    print('%d %s %d = %d' % (x, op, y, x+y))
elif op == '-':
    print('%d %s %d = %d' % (x, op, y, x-y))
elif op == '*':
    print('%d %s %d = %d' % (x, op, y, x*y))
elif y == 0:
    print('Não é possível dividir por zero!')
else:
    print('%d %s %d = %d' % (x, op, y, x/y))
