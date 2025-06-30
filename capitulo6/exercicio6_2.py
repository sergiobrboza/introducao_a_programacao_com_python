'''Faça um programa que leia duas listas e que gere uma terceira lista
com os elementos das duas primeiras'''
lista1 = [0, 0, 0]
lista2 = [0, 0, 0]
lista3 = []
x= 0
while x < 3:
    lista1[x] = int(input(f"Adicione um numero inteiro na posiçao {x}"))
    lista2[x] = int(input(f"Adicione um numero inteiro na posiçao {x}"))
    x +=1

lista3.extend(lista1)
lista3.extend(lista2)

x = 0
for x in lista3:
    print(f"Posiçao {x}: {lista3[x]}")
