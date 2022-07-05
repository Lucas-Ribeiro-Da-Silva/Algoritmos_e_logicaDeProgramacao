# 1) Crie um registro do tipo Carro em que os seguintes campos estejam presentes:
#   - marca do carro (string)
#   - ano do carro (int)
#   - preço de carro (float)
#   - bicombustivel (True ou False)

class Carro:
    def __init__(self, mc, ac, pc, bi):
        self.marca = mc
        self.ano = ac
        self.preco = pc
        self.bicombustivel = bi

# 2) Elabore um programa que crie duas variáveis do tipo Carro inicializando-as com os dados.
#    Observação: os dados também podem ser provenientes de entradas do usuário.

c1 = Carro('Ferrari', 2012, 1_000_000, False) # inicialização com dados de constantes.

marca = input('Marca? ')
ano = int(input('Ano? '))
preco = float(input('Preço? '))
bicombustivel = input('Bicombustivel (s/n)? ')

c2 = Carro(marca, ano, preco, bicombustivel == 's') #inicialização com dados de variáveis.

# 3) Altere o preço dos carros para 10% a mais.

c1.preco = c1.preco * 1.10
c2.preco = c2.preco * 1.10

# 4) Altere o ano dos carros para 2022.

c1.ano = 2022
c2.ano = 2022

# 5) Faça uma verificação em um dos carros para saber se ele aceita mais de um
#    tipo de combustível. Exiba uma mensagem indicativa.

if c2.bicombustivel:
    print('Aceita mais de um tipo de combustível!')
else:
    print('Só aceita um tipo de combustível!')

# 6) Altere a marca de um dos carros para 'Tesla'. E exiba todos os dados do carro alterado.

c1.marca = 'Tesla'
print('Marca:', c1.marca)
print('Ano:', c1.ano)
print('Preço:', c1.preco)
print('Bicombustível:', 'sim' if c1.bicombustivel else 'não')
