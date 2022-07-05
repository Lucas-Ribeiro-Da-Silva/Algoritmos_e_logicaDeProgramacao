"""
11. def letra(n):
# Recebe: um valor inteiro n (1 <= n <= 26).
# Retorna: a letra maiúscula correspondente à n no alfabeto (1 equivale à 'A',
 2 à 'B',..., 26 à 'Z').
# Obs: usar as funções built-in chr() e/ou ord() para ajudar.
"""

# ord('A') == 65
def letra(n):
    return  chr(n+64)
print(letra(26))
