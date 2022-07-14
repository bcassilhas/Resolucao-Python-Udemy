## Exercício 45  - Seção 4

letra = input("Digite uma letra em formato maiúsculo:")
## Considerando apenas a primeira letra do input e forçando o tipo maiúsculo:
letra = letra[0].upper()
## Fazendo a conversão via ASCII:
print(f"A letra {letra} em minúsculo é {chr(ord(letra) + 32)}.")










