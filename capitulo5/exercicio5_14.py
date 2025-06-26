'''Escreva um programa que leia números inteiros do teclado. O programa deve exibir o maior e o menor número digitado. A leitura deve ser encerrada quando o usuário digitar o número zero.'''
numeros = []

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
