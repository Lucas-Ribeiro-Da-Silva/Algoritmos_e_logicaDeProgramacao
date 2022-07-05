#[EXERCÍCIO 7] Com base no Exemplo 6, crie uma versão em que não existam estruturas de seleção aninhadas. Obs.: use elif.

x = input('caractere: ')
if x=='0' or x=='2' or x=='4' or x=='6' or x=='8':
    print('\'%s\' é um dígito par' % x)
elif x=='1' or x=='3' or x=='5' or x=='7' or x=='9':
    print('\'%s\' é um dígito ímpar' % x)
elif x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
    print('\'%s\' é uma letra vogal minúscula' % x)
elif 'a'<=x<='z' and (x!='a' and x!='e' and x!='i' and x!='o' and x!='u'):
    print('\'%s\' é uma letra consoante minúscula' % x)
elif x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
    print('\'%s\' é uma letra vogal maiúscula' % x)
else:
    print('\'%s\' é uma letra consoante maiúscula' % x)
