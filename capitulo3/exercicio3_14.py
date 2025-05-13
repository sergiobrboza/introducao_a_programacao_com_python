# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro 
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por 
# dia e R$ 0,15 por km rodado.

km_percorrido = float(input("Informe quantos Km foram percorridos: "))
dias_alugados = int(input("Informe quantos dias foi alugado o carro: "))

preco = (km_percorrido * 0.15) + (dias_alugados * 60)

print(f"O cliente deverá pagar: R${preco:.2f}")