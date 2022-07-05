#11. Dado um inteiro 𝑛, exibir o dia da semana correspondente (domingo = 1 e sábado = 7) ou 'dia inválido'

n = int(input("digite um número: "))

if n==1: print('domingo')
elif n==2: print('segunda')
elif n==3: print('terça')
elif n==4: print('quarta')
elif n==5: print('quinta')
elif n==6: print('sexta')
elif n==7: print('sabádo')
else: print('dia inválido')