# Escreva um programa que leia a quantidade de dias, horas minutos,
# segundos do usuário. Calcule o total em segundos.

dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

calcula_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print("Total de segundos: ", calcula_segundos)