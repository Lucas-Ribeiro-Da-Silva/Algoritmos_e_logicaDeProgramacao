"""
Q1. Crie a função soma(inicio,fim,passo) que recebe como argumentos três valores inteiros e retorna a soma dos inteiros
do intervalo fechado crescente [inicio..fim] pulando de passo em passo. A função deve funcionar idêntico ao ilustrado.
Restrições:
(I)suponha que passo será positivo;
(II) só um laço;
(III) não use funções pré-definidas;
(IV) só recursos dados em aula.
"""

def soma(inicio,fim,passo):
    soma = 0
    for i in range(inicio,fim+1,passo):
        soma += i
    return soma

print(soma(-3, 9, 3))

