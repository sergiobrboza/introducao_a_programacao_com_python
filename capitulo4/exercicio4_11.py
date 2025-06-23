"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

"""
valor_casa = int(input("Informe o valor da casa: R$"))
salario = int(input("Informe o seu salário: R$"))
anos_pagar = int(input("Informe os anos a pagar: "))
total_meses = anos_pagar * 12
prestacao_mensal = valor_casa / total_meses
limite = salario * 0.30

print(f"\nValor da prestação: R${prestacao_mensal:.2f}")
print(f"30% do seu salário: R${limite:.2f}")

if prestacao_mensal <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")
