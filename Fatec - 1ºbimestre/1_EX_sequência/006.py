# 6. Dado um salΓ‘rio atual em reais e uma idade em anos,
# calcular o novo salΓ‘rio, que serΓ‘ o salΓ‘rio atual acrescido da idade em porcentagem.
# Exemplo: π ππΓ‘πππ ππ‘π’ππ = π$ 1000,00 e πππππ = 23,
# logo, πππ£π π ππΓ‘πππ = π$ 1000,00 + 23% ππ π$ 1000,00 = π$ 1230,00.
# Exiba apenas o novo salΓ‘rio.

salario = float(input("Digite seu salario: "))
idade = int(input("Digite sua idade: "))
acres = idade/100
novo_salario = salario+acres*salario
print("O novo salΓ‘rio Γ© R$%.2f" % novo_salario)