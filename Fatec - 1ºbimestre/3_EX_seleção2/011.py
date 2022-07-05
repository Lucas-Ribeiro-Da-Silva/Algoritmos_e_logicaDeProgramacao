#[EXEMPLO 6] Com base no Exemplo 5, crie uma versão em que o caractere x
#também possa ser uma letra maiúscula e tenha a respectiva indicação.

x = input('caractere: ')
if '0' <= x <= '9':
    print('\'%s\' é um dígito' % x, end=' ')
    if x=='0' or x=='2' or x=='4' or x=='6' or x=='8':
        print('par')
    else:
        print('ímpar')
else:
    print('\'%s\' é uma letra' % x, end=' ')
    if 'a' <= x <= 'z':
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            print('vogal minúscula')
        else:
            print('consoante minúscula')
    else:
        if x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
            print('vogal maiúscula')
        else:
            print('consoante maiúscula')
