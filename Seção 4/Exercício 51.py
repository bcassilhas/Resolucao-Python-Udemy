## Exercício 52  - Seção 4

inv1 = float(input("Digite quanto o primeiro amigo investiu:"))
inv2 = float(input("Digite quanto o segundo amigo investiu:"))
inv3 = float(input("Digite quanto o terceiro amigo investiu:"))
prem = float(input("Qual o valor do prêmio? R$"))
tot_int = inv1+inv2+inv3

print(f"O primeiro amigo, que investiu R${inv1}, ganharia R${(inv1/tot_int)*prem:.2f}.")
print(f"O segundo amigo, que investiu R${inv2}, ganharia R${(inv2/tot_int)*prem:.2f}.")
print(f"O terceiro amigo, que investiu R${inv3}, ganharia R${(inv3/tot_int)*prem:.2f}.")












