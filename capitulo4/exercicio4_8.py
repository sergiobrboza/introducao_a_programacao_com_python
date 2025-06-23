"""
Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
"""
plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50
else :
    if plano == "Falomuito":
        minutos_no_plano = 500
        extra = 0.15
        preco = 99
    else:
        print("Não conheço esse plano")