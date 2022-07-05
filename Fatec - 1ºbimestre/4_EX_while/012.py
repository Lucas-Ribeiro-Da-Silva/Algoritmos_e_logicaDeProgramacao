#[EXEMPLO 6] Crie um programa que receba dois números inteiros a e b e um caractere op
# representando um operador aritmético (+, -, * ou /) e exiba o inteiro resultante da expressão
#a op b. O programa deve executar o procedimento enquanto o usuário desejar ou até a ocorrência de uma divisão inválida.

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
            break
        else:
            r = a/b
    print('%d %c %d = %d\n' % (a,op,b,r))
    e = input('Calcular? ')
