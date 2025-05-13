# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_dia = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Informe quantos anos voce fuma: "))

minutos_perdidos = (cigarros_dia * 10) * (anos_fumando * 365)

dias_perdidos = minutos_perdidos / 1440
print(f"Você perdeu cerca de {dias_perdidos:.2f} dias da sua vida")