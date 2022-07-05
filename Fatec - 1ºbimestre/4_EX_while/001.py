#[EXEMPLO 1] Crie um programa que receba dois números inteiros a (a>=0) e b
#(b>0) e calcule o quociente da divisão inteira a por b. Observação, não use
#operadores de divisão, produto e resto.

a = int(input('a: '))
b = int(input('b: '))
q = 0
while a >= b:
    a -= b
    q += 1
print('Quociente:', q)
