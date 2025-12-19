'''

Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que 
também será procurado. Na impressão, indique qual dos dois foi achado primeiro.

L = [15, 7, 27, 39]
p = int(input('Digite o valor à procurar: '))
x = 0

while x < len(L) and L[x] != p:
    x += 1

if x < len(L):
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')

'''

L = [15, 7, 27, 39]
p = int(input('Digite o primeiro valor à procurar: '))
v = int(input('Digite o segundo valor à procurar: '))

x = 0

while x < len(L) and L[x] != p and L[x] != v:
    x += 1

if x < len(L):
    if L[x] == p:
        print(f'{p} foi achado primeiro na posição {x}')
    else:
        print(f'{v} foi achado primeiro na posição {x}')
else:
    print('Nenhum dos dois valores foi encontrado')
