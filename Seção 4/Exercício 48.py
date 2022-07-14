## Exercício 49  - Seção 4

horario = input("Digite o horário no formato hh:mm:ss >")
## Extraindo as horas, minutos e segundos do String e convertendo em inteiro:
hr = int(horario[0:2])
min = int(horario[3:5])
seg = int(horario[6:8])
print(f"Hora inicial: {hr}:{min}:{seg}")
duracao = int(input("Digite a duração do experimento (em segundos): "))
## Somar os segundos da duração nos segundos do horário:
seg += duracao
## Transformar o valor de segundos maior que 60 em minuto(s) e adicionar aos minutos já existentes:
min += seg // 60
## Deixar o campo dos segundos apenas com o que não foi possível converter em minuto (menos que 60s):
seg = int(seg % 60)
## Transformar o valor de minutos maior que 60 em hora(s) e adicionar as horas já existentes:
hr += min // 60
## Deixar o campo dos minutos apenas com o que não foi possível converter em hora (menos que 60m):
min = int(min % 60)
print(f"A hora de término do experimento foi: {hr}:{min}:{seg}.")










