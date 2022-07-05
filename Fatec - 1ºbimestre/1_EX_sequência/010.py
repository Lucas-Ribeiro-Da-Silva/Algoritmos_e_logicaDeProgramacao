# 10. Calcule a nota final de um aluno sabendo que ela é composta da seguinte forma:
# 𝑃𝑟𝑜𝑣𝑎 1 (40%) + 𝑃𝑟𝑜𝑣𝑎 2 (40%) + 𝑇𝑟𝑎𝑏𝑎𝑙ℎ𝑜𝑠 (20%).
# Os três valores que compõem a nota final serão informados pelo usuário, exiba-a com duas casas decimais.

p1 = float(input("Digite a nota: "))
p2 = float(input("Digite a nota: "))
t = float(input("Digite a nota: "))

final = p1*0.4 + p2*0.4 + t*0.2

print("A nota final é %.2f" % final)