# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
lista1 = [1,23,3,5,6,72,9,2]
lista2 = [1,2,3,4,5,6,7,8,10]
lista3 = list(set(lista1 + lista2))
print(lista3)