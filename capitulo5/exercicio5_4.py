'''Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas apenas os números pares.'''
x = 2
y = int(input("Informe um numero: "))

while x <= y:
    if x % 2 == 0:
        print(x)
    x += 1