"""
Q4. Complete as lacunas do registro Livro que contém os campos titulo, ano e preco e o programa que o utiliza.
Se completado corretamente, o programa funcionará idêntico ao ilustrado.
Restrições: (I) só recursos dados em aula.
"""

class Livro:
    def __init__(self, t, a, p):
        self.titulo = t
        self.ano = a
        self.preco = p

L = Livro('Harry Potter', 1997, 26.99)
print('Titulo: %s\nPreço: R$ %.2f' % (L.titulo, L.preco))
