'''Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501'''
numero = input("Digite um número: ")

if numero == numero[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
