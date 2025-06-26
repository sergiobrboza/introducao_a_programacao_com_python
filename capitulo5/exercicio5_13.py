'''Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.'''

divida = float(input("Digite o valor inicial da dívida: R$ "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))
pagamento_mensal = float(input("Digite o valor que será pago mensalmente: R$ "))

juros_mensal = juros_mensal / 100
meses = 0
total_pago = 0
divida_original = divida

if pagamento_mensal <= divida * juros_mensal:
    print("O valor do pagamento mensal é muito baixo para cobrir os juros. A dívida nunca será quitada.")
else:
    while divida > 0:
        divida += divida * juros_mensal    
        pagamento = min(pagamento_mensal, divida) 
        divida -= pagamento
        total_pago += pagamento
        meses += 1

    total_juros = total_pago - divida_original

    print("\nNúmero de meses para quitar a dívida:", meses)
    print("Total pago: R$ {:.2f}".format(total_pago))
    print("Total de juros pagos: R$ {:.2f}".format(total_juros))
