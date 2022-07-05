# 7. Fornecidos os coeficientes de uma equação de segundo grau
# (com 𝑎 ≠ 0, ou seja, não é necessário verificar a existência da equação), exibir suas raízes.
# Obs.: Caso Δ seja negativo, imprimir as raízes no formato 𝑥 − 𝑦𝑖 e 𝑥 + 𝑦𝑖, após calcular 𝑥 e 𝑦

a = int(input('coeficiente a != de 0: '))
b = int(input('coeficiente 2: '))
c = int(input('coeficiente 3: '))

# delta = b^2 - 4 *a *c
# x = -b +- raiz de delta / 2*a

delta = b ** 2 - 4 * a * c
x1 = (-(b) + (delta ** 0.5)) / (2 * a)
x2 = (-(b) - (delta ** 0.5)) / (2 * a)

if delta >= 0:
    print('x1=%.d' % x1)
    print('x2=%.d' % x2)
else:
    y = -delta
    x1 = (-(b) + (y ** 0.5)*((-1)**0.5)) / (2 * a)
    x2 = (-(b) - (y ** 0.5)*((-1)**0.5)) / (2 * a)
    print('raiz um é ', x1)
    print('raiz dois é', x2)

