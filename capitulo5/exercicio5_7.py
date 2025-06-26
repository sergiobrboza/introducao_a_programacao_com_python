'''Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.'''
n = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o número inicial da tabuada: "))
fim = int(input("Digite o número final da tabuada: "))

x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x += 1
