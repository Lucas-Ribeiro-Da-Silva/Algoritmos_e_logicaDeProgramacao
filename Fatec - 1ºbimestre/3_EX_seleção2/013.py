#[EXERCÍCIO 8] Altere a solução do Exercício 7 de modo que se x não for dígito, letra
# minúscula ou letra maiúscula o programa exiba 'caractere desconhecido'.

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
elif 'A'<=x<='Z' and (x!='A' and x!='E' and x!='I' and x!='O' and x!='U'):
    print('\'%s\' é uma letra consoante maiúscula' % x)
else:
    print('caractere desconhecido')
