"""
Q2. Considerando a função misterio(a,b,c), assinale a alternativa que representa a sequência de valores que as variáveis
locais e, f, g e h receberão caso a função seja chamada com os parâmetros a=10, b=[2,4,6,7,11,15,17,20]e c=8.
"""
def misterio(a, b, c):
    d = False
    e = 0
    f = 0
    g = c-1 #7
    while (f<=g) and (not d):
        h = (f+g)//2 #0+7//2 = 3     4+7//2=5   4+4//2=4
        e += 1 #1   2   3
        if a == b[h]: d = True #b[3]=7    b[5]=15   b[4]=11
        elif a < b[h] : g = h-1 #7=5-1=4     4=4-1=3
        else: f = h+1 #3+1=4
    return e

print(misterio(10, [2, 4, 6, 7, 11, 15, 17, 20], 8))

