"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.
"""

distancia = float(input("Informe a distacia que pretende percorrer (Km): "))

if distancia <= 200:
    valor = distancia * 0.5
    print(f"Você irá pagar R${valor:.2f} para percorrer {distancia}Km")

else:
    valor = distancia * 0.45
    print(f"Você irá pagar R${valor:.2f} para percorrer {distancia}Km")