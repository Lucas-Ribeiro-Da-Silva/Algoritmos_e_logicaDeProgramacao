#1. Fornecido o preço unitário e a quantidade de uma determinada peça, calcular e exibir o total a pagar sabendo que haverá um desconto de 10%

preco = float(input("Digite o preço unitário: "))
qtd = int(input("Digite a quantidade de produtos: "))
desc = 0.9 #10%
total = preco * qtd * desc
print("O total a pagar é R$ %.2f" % total)

#ou por este modo

preco = float(input("Digite o preço unitário: "))
qtd = int(input("Digite a quantidade de produtos: "))
desc = 0.1 #10%
total = preco * qtd - desc * preco * qtd
print("O total a pagar é R$ %.2f" % total)

#ou outro meio de interpolar
#print('Total a pagar R${:.2f}' .format(total))




# Crie um programa que receba como entrada o valor total
# de uma compra, a quantidade de parcelas em que o total
# será dividido e o juros do parcelamento, isto é, a
# porcentagem a mais que será cobrada em cada parcela.
# O programa deverá exibir: (I) o valor final de uma das
# parcelas; (II) o valor da parcela que corresponde ao juros
# e; (III) o valor final da compra parcelada



"""
valor_total = float(input('valor total da compra: '))
qtd = int(input('quantidade de parcelas: '))
juros = float(input('juros cobrado: '))

valor_parcelamento = valor_total / qtd
valor_juros = valor_parcelamento * (juros/100)
valor_parcela = valor_parcelamento + valor_juros
valor_final = (valor_parcelamento + valor_juros) * qtd

print ("Valor das parcelas: %.2f" % valor_parcela)
print ("Valor dos juros: %.2f" % valor_juros)
print ("Valor Final: %.2f" % valor_final)

"""

#resolução
compra = float(input('Valor da compra? R$ '))
qtd_parcelas = int(input('Quantas parcelas?'))
p_juros = float(input('Juros por parcela? '))

parcela_sj = compra / qtd_parcelas
v_juros = p_juros/100 * parcela_sj
parcela_cj = parcela_sj + v_juros

print("Valor final da parcela = R$ %.2f" % parcela_cj)
print("Valor do juros = R$ %.2f" % v_juros)
print('Valor final da comopra = R$ %.2f' % (parcela_cj * qtd_parcelas))

