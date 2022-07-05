#[EXERCÍCIO 2] Crie um programa que receba um caractere c e exiba uma mensagem
#indicando se c é uma vogal, uma consoante ou se não é uma letra. Considere apenas
#letras de nosso alfabeto ('A'...'Z' e 'a'...'z') e sem acentuação.

c = input('Caractere: ')
if 'a'<=c<='z' or 'A'<=c<='Z':
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or \
        c=='A' or c=='E' or c=='I' or c=='o' or c=='U':
         print('Vogal')
    else:
        print('Consoante')
else:
    print('Não é uma letra')

