'''
Modifique o programa do exercicio 6.9 de forma a pesquisar p e v em toda a lista e informando ao usuário a posição onde p e a posição onde v foram encontrados
'''

L = [15, 7, 27, 39]
p = int(input('Digite o valor p a procurar: '))
v = int(input('Digite o valor v a procurar: '))

xp = 0
xv = 0
achou_p = False
achou_v = False
x = 0

while x < len(L):
    if L[x] == p and not achou_p:
        xp = x
        achou_p = True

    if L[x] == v and not achou_v:
        xv = x
        achou_v = True

    x += 1

if achou_p:
    print(f'{p} encontrado na posição {xp}')
else:
    print(f'{p} não encontrado')

if achou_v:
    print(f'{v} encontrado na posição {xv}')
else:
    print(f'{v} não encontrado')
