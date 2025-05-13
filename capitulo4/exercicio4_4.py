"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários inferiores ou iguais a R$ 1.250, calcule um aumento de 10%; para os superiores, de 15%.
"""
salario = float(input("Informe o seu salário: R$"))

if salario <= 1250:
    novo_salario = (salario * 0.10) + salario
    print(f"O seu novo salário é: R${novo_salario:.2f}")

else:
    novo_salario = (salario * 0.15) + salario
    print(f"O seu novo salário é: R${novo_salario:.2f}")