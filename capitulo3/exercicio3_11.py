# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco = float(input("Informe o preço da mercadoria: "))
desconto = int(input("Informe a porcentagem de desconto: "))

valor_desconto = preco * desconto / 100
novo_preco = valor_desconto + preco
print(f"O valor do desconto: R${valor_desconto:.2f} \nO novo preço: R${novo_preco:.2f}")