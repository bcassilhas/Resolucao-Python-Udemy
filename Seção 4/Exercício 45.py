## Exercício 46  - Seção 4
## INT para não aceitar letras nesse campo:
num = int(input("Digite um número inteiro de três digitos:"))
## Transformando em String para considerar apenas os primeiros 3 digitos, caso seja colocado um número maior:
num = str(num)[:3]
## Invertendo o número:
numinvert = (num)[::-1]
print(f"O número {num} invertido é o {numinvert}")





