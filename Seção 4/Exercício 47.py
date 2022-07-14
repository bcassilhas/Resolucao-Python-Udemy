## Exercício 48  - Seção 4

seg = int(input("Digite um valor em segundos:"))
hr = seg // 3600
min = (seg % 3600) // 60
segresto = ((seg % 3600) % 60)

print(f"{seg} s = {hr}:{min}:{segresto}")







