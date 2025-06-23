"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (−), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
"""
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo numero: "))
operacao = input("somar(+), subtrair(-), multiplicar(*) ou dividir(/): ")

if operacao == "+" :
    resultado = a + b

elif operacao == "-":
    resultado = a - b

elif operacao == "*":
    resultado = a * b

elif operacao == "/":
    resultado = a / b

print(f"{a} {operacao} {b} = {resultado}")
    