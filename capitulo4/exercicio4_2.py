""" 
Escreva um programa que pergunte a velocidade do carro de um 
usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80Km/h.
"""

velocidade = int(input("Informe a velocidade do seu veiculo: "))

if velocidade > 80:
    print("Você foi multado!")
    valor_multa = (velocidade - 80) * 5
    print(f"E deverá pagar: R${valor_multa:.2f}")
else:
    print("Você está dentro do limite!")