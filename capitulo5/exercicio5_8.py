'''Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = 0
contador = 0

while contador < b:
    resultado = resultado + a
    contador = contador + 1

print(f"{a} x {b} = {resultado}")

