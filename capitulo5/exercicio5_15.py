'''Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:

mathematica
Copiar
Editar
Código  | Preço
1       | 0.50
2       | 1.00
3       | 4.00
5       | 7.00
9       | 8.00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".'''
precos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00
}
total = 0.0

while True:
    codigo = int(input("Digite o código do produto (0 para encerrar): "))

    if codigo == 0:
        break

    if codigo in precos:
        quantidade = int(input("Digite a quantidade comprada: "))
        total += precos[codigo] * quantidade
    else:
        print("Código inválido.")

print(f"\nTotal da compra: R$ {total:.2f}")
