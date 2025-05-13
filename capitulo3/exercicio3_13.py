# Escreva um programa que converta uma temperatura digitada
# em °C em °F.

temperatura_celsius = float(input("Informe a temperatura em °C: "))
temperatura_fahrenheit = temperatura_celsius * 1.8 + 32
print(f"{temperatura_celsius:.1f}°C = {temperatura_fahrenheit:.1f}°F")