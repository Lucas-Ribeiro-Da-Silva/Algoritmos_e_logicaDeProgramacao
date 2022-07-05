#[EXEMPLO 5] Crie um programa que leia um caractere x e indique se x é um dígito
#ou uma letra. Se x é dígito, indique se representa um par ou ímpar, se letra, se
#representa uma vogal ou consoante. Obs.: x será apenas dígito ou minúscula.

x = input('caractere: ')
if '0' <= x <= '9':
    print('\'%s\' é um dígito' % x, end=' ')
    if x=='0' or x=='2' or x=='4' or x=='6' or x=='8':
        print('par')
    else:
        print('ímpar')
else:
    print('\'%s\' é uma letra' % x, end=' ')
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print('vogal')
    else:
        print('consoante')
