# 10. Calcule a nota final de um aluno sabendo que ela Γ© composta da seguinte forma:
# ππππ£π 1 (40%) + ππππ£π 2 (40%) + ππππππβππ  (20%).
# Os trΓͺs valores que compΓ΅em a nota final serΓ£o informados pelo usuΓ‘rio, exiba-a com duas casas decimais.

p1 = float(input("Digite a nota: "))
p2 = float(input("Digite a nota: "))
t = float(input("Digite a nota: "))

final = p1*0.4 + p2*0.4 + t*0.2

print("A nota final Γ© %.2f" % final)