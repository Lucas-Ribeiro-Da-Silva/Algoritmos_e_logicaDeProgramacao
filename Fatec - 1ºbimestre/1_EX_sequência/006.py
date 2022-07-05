# 6. Dado um salário atual em reais e uma idade em anos,
# calcular o novo salário, que será o salário atual acrescido da idade em porcentagem.
# Exemplo: 𝑠𝑎𝑙á𝑟𝑖𝑜 𝑎𝑡𝑢𝑎𝑙 = 𝑅$ 1000,00 e 𝑖𝑑𝑎𝑑𝑒 = 23,
# logo, 𝑛𝑜𝑣𝑜 𝑠𝑎𝑙á𝑟𝑖𝑜 = 𝑅$ 1000,00 + 23% 𝑑𝑒 𝑅$ 1000,00 = 𝑅$ 1230,00.
# Exiba apenas o novo salário.

salario = float(input("Digite seu salario: "))
idade = int(input("Digite sua idade: "))
acres = idade/100
novo_salario = salario+acres*salario
print("O novo salário é R$%.2f" % novo_salario)