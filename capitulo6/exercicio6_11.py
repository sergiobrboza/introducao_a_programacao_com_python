'''

Modifique o programa 6.6 usando for. Explique por que nem todos os while podem ser transformados em for.

L = []
while True:

    n = int(input('Digite um valor (0 sai): '))

    if n == 0:
        break
        
    L.append(n)

x = 0

while x < len(L):
    print(L[x])
    x+=1


'''

L = []

acao = int(input('Informe quantos numeros deseja inserir: '))

for i in range(acao):
    p = int(input('digite um numero: '))
    L.append(p)

for i in L:
    print(i)


