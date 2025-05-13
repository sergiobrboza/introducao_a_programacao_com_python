# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distancia a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Informe a distancia percorrer em Km: "))
velocidade_media = int(input("Informe a velocidade média em Km/h: "))

calcula_tempo = distancia / velocidade_media
print(f"O tempo da viagem será de {calcula_tempo:.2f} horas")