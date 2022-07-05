#[EXEMPLO 2] Crie um programa que receba o preço de um produto e a quantidade
#comprada. Se o total for maior do que R$ 200,00 o cliente optará por um desconto
#de 5% ou parcelamento em 4 vezes sem juros. O programa deverá exibir o valor do
#desconto ou das parcelas, se aplicável, e o total final.

preco = float(input('Preço do produto: '))
qtd = int(input('Quantidade: '))
total = preco * qtd
if total > 200.00:
    opcao = input('Desconto [D] ou parcelamento [P]: ')
    if opcao=='D':
        desc = 0.05*total
        total -= desc
        print('Desconto de R$ %.2f' % desc)
    else:
        print('4 parcelas de R$ %.2f' % (total/4))
print('Total: R$ %.2f' % total)

