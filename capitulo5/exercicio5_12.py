'''Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.'''
deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
deposito_mensal = float(input("Digite o valor depositado todo mês: R$ "))

taxa_juros = taxa_juros / 100
saldo = deposito_inicial
total_investido = deposito_inicial

print("\nMês\tSaldo")
print("-------------------")

for mes in range(1, 25):
    saldo += deposito_mensal         
    total_investido += deposito_mensal
    saldo += saldo * taxa_juros      
    print(f"{mes:2}\tR$ {saldo:.2f}")

ganho_juros = saldo - total_investido

print("\nTotal investido: R$ {:.2f}".format(total_investido))
print("Total ganho com juros: R$ {:.2f}".format(ganho_juros))
