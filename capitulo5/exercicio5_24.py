'''Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.'''
n = int(input("Quantos números primos você quer? "))
contador = 0
numero = 2

while contador < n:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero, end=" ")
        contador += 1
    numero += 1
