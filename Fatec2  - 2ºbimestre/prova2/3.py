"""
Q3. Crie a função negativos(a,L,C) que retorna a soma dos itens negativos da matriz numérica a de formato L×C (L>0 e C>0).
Deve funcionar idêntico ao ilustrado. Restrições:
(I) use dois for;
(II) não use funções pré-definidas;
(III) só recursos dados em aula.
"""

def negativos(a,L,C):
    soma = 0
    for i in range(L):
        for j in range(C):
            if a[i][j] < 0: soma +=a[i][j]
    return soma

a = [[95, -20, -10, 7], [3, -30, 49, 90], [66, 73, 93, -40]]
print(negativos(a, 3, 4))