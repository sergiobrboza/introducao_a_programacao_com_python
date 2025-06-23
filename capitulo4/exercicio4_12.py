"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela:
"""
kwh = float(input("Informe a quantidade de kWh consumida: "))
tipo = input("Informe o tipo de instalação (R = Residencial, C = Comercial, I = Industrial): ").strip().upper()

if tipo == 'R':
    if kwh <= 500:
        preco_kwh = 0.40
    else:
        preco_kwh = 0.65
elif tipo == 'C':
    if kwh <= 500:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
elif tipo == 'I':
    if kwh <= 500:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
else:
    print("Tipo de instalação inválido.")
    preco_kwh = None

if preco_kwh is not None:
    total = kwh * preco_kwh
    print(f"\nTipo de instalação: {tipo}")
    print(f"Consumo: {kwh} kWh")
    print(f"Preço por kWh: R${preco_kwh:.2f}")
    print(f"Total a pagar: R${total:.2f}")
