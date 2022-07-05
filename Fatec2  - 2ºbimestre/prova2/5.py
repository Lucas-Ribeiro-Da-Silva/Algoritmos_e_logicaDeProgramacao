"""
Crie a função maiusculas(v,n) que recebe como parâmetro um vetor de caracteres v e seu tamanho n, a função deve exibir
apenas os caracteres de v que são maiúsculas não acentuadas. A função deve funcionar idêntico ao ilustrado.
Restrições:
(I) não crie outros vetores/strings;
(II) considere apenas nosso alfabeto latino;
(III) só um loop;
(IV) use while;
(V) só recursos dados em aula
"""

def maiusculas(v,n):
    i = 0
    while i < n:
        if v[i]>= 'A' and v[i] <= 'Z':
            print(v[i], end= ' ')
        i += 1

v = ['i', '!', 'A', '3', 'E']
maiusculas(v, 5)

v = ['E', 'X', 'E', '*']
maiusculas(v, 4)

