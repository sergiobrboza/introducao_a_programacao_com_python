'''Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.'''
a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

resto = a
while resto >= b:
    resto -= b

print(f"Resto da divisão: {resto}")
