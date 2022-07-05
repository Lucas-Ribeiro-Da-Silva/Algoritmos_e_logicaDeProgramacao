"""
Exercicios
"""
'''
#7

def impar_1(n):
    if n % 2 != 0:
        return True
    else:
        return False

#versão aluno da Fatec

def impar_2(n)
    return n%2 == 1
'''


'''
#10

def triangulo(a, b, c):
    if a<b+c and b<a+c and c<a+b:
        return True
    else:
        return False
##############################################################
def triangulo1(a, b, c):
    return a<b+c and B<a+c and c<a+b

def tipo_triangulo(a, b, c):
    if a==b and b==c:
        return 'Equilatero'
    elif a==b or b==c or a==c:
        return 'Isósceles'
    else:
        return 'Escaleno'

x = int(input('x?'))
y = int(input('y?'))
z = int(input('z?'))

if triangulo(x, y, z):
    print('Formam um triangulo: %s' % tipo_trianguo(x, y, z))
else:
    print('Não formam um triângulo')
'''


#9
def primo(n):
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
    if qtd == 2:
        return True
    else:
        return False

for n in range(2, 21):
    print(n, primo(n))


#mudança versão Melhorada

def primo(n):
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
    return qtd == 2

for n in range(2, 21):
    print(n, primo(n))

#dnv

def primo(n):
    qtd = 0
    for i in range(2, n):
        if n % i == 0:
            qtd += 1
    return qtd == 0

for n in range(2, 21):
    print(n, primo(n))

#mais uma

def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(2, 21):
    print(n, primo(n))


# 123_456 --> _ é usado para visualmente compreender os numeros
    
