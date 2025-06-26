'''Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.'''
deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))

taxa_juros = taxa_juros / 100
saldo = deposito_inicial

print("\nMês\tSaldo")
print("-------------------")
for mes in range(1, 25):
    juros = saldo * taxa_juros
    saldo += juros
    print(f"{mes:2}\tR$ {saldo:.2f}")

ganho_juros = saldo - deposito_inicial
print("\nTotal ganho com juros: R$ {:.2f}".format(ganho_juros))
