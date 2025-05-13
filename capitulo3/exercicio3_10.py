# Faça um programa que calcule o aumento de um salário. Ele
# deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input("Informe o salário: R$"))
porcentagem = float(input("Informe a porcentagem de aumento: "))

valor_aumento = salario * porcentagem / 100
novo_salario = valor_aumento + salario
print(f"O valor do aumento: R${valor_aumento:.2f} \nO novo salário: R${novo_salario:.2f}")