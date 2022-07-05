#12. Fornecidas as áreas de um círculo e de um quadrado,
# exibir 'esconde' se for possível ocultar completamente o quadrado sob o círculo,
# ou 'não esconde', caso contrário (adote 𝜋 = 3,14)

l = float(input('Qual o valor do lado L do quadrado?'))
r = float(input('Qual o valor do raio R do círculo?'))
PI = 3.14

areaQ = l**2
areaC = PI * (r**2)

if areaC<areaQ: print('esconde')
else: print('não esconde')
