#[EXERCÍCIO 7] Altere o programa do Exemplo 6 para que caso ocorra uma divisão inválida o usuário possa inserir
# novos operandos e continuar a execução.

e = input('Calcular? ')
while e=='s':
    a = int(input('a: '))
    b = int(input('b: '))
    op = input('operador: ')
    if op=='+': r = a+b
    elif op=='-': r = a-b
    elif op=='*': r = a*b
    elif op=='/':
        if b==0:
            print('Divisão por zero!')
            continue
        else:
            r = a/b
    print('%d %c %d = %d\n' % (a,op,b,r))
    e = input('Calcular? ')
