"""
[EXEMPLO 1] Crie um programa que exiba todos os segundos de um minuto. O
primeiro segundo exibido será 0 e o último 59.
"""

s = 0
while s < 60:
    print(s)
    s += 1
################
for s in range(60):
    print(s)

"""
[EXEMPLO 2] Altere o programa do Exemplo 1 de modo que os segundos
sejam exibidos no formato de um relógio digital, ou seja, hh:mm:ss.
"""

s = 0
while s < 60:
    print('00:00:%02d' % s)
    s += 1


for s in range(60):
    print('00:00:%02d' % s)

"""
[EXEMPLO 3] Altere o programa do Exemplo 2 para que use a função sleep()
da biblioteca time e aguarde 1 segundo entre as exibições.
"""

from time import sleep
s = 0
while s < 60:
    print('00:00:%02d' % s)
    s += 1
    sleep(1)



from time import sleep
for s in range(60):
    print('00:00:%02d' % s)
    sleep(1)


"""
[EXEMPLO 4] Altere o programa do Exemplo 3 de modo que a cada 60
segundos o mostrador de minutos seja incrementado e o de segundos zerado.
Repita o procedimento até completar 00:59:59.
"""
from time import sleep
m = 0
while m < 60:
    s = 0
    while s < 60:
        print('00:%02d:%02d' % (m, s))
        s += 1
        sleep(1)
    m += 1



"""
[EXEMPLO 4] Altere o programa do Exemplo 3 de modo que a cada 60
segundos o mostrador de minutos seja incrementado e o de segundos zerado.
Repita o procedimento até completar 00:59:59.
"""
from time import sleep
for m in range(60):
    for s in range(60):
        print('00:%02d:%02d' % (m, s))
        sleep(1)

"""
[EXEMPLO 5] Altere o programa do Exemplo 4 de modo que a cada 60
minutos o mostrador de horas seja incrementado e o de minutos zerado.
Repita o procedimento até completar 23:59:59.

"""

from time import sleep
h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print('%02d:%02d:%02d' % (h, m, s))
            s += 1
            sleep(1)
        m += 1
    h += 1

############

from time import sleep
for h in range(24):
    for m in range(60):
        for s in range(60):
            print('%02d:%02d:%02d' % (h, m, s))
            sleep(1)