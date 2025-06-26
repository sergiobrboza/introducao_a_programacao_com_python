'''O que acontece se digitarmos 0,001 para aceitar valores decimais, e não funcionar, altere-o de forma a corrigir o problema.

'''
valor = float(input("Digite o valor a pagar: "))
valor_milésimos = int(round(valor * 1000))  # 

moedas = 0
atual = 100000
apagar = valor_milésimos

while True:
    if atual <= apagar:
        apagar -= atual
        moedas += 1
    else:
        if moedas > 0:
            print(f"{moedas} unidade(s) de R${atual / 1000:.3f}")
        if apagar == 0:
            break
        if atual == 100000:
            atual = 50000
        elif atual == 50000:
            atual = 20000
        elif atual == 20000:
            atual = 10000
        elif atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 200
        elif atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        moedas = 0
