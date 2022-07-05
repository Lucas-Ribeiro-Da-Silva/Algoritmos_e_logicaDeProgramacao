"""
8. Fornecido um número inteiro 𝑛 (𝑛 ≥ 0) em decimal, exibir seu correspondente em binário (monte o
binário usando apenas adição, subtração, multiplicação e/ou divisão).
Exemplo: Entrada: 13 → Saída: 1101
"""

#CERTO MAS ERRADO, NÃO PODIA USAR DOIS LAÇOS JUNTOS

n = int(input("n?"))
x = ''
while n>0:
    #conversão decimal -> binário:
    resultado = n % 2
    n = n // 2
    #print(resultado, end='')
    x = str(x) +  str(resultado)

#invertendo para a ordem correta
x = int(x)
while x>0:
    num = x%10
    print(num, end='')
    x = x//10



