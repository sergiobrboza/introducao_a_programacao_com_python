'''Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.'''
while True:
    print("\nMenu de Operações:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == "5":
        print("Saindo do programa.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    numero = int(input("Digite o número para gerar a tabuada: "))

    print(f"\nTabuada de {numero}:")

    for i in range(1, 11):
        if opcao == "1":
            print(f"{numero} + {i} = {numero + i}")
        elif opcao == "2":
            print(f"{numero} - {i} = {numero - i}")
        elif opcao == "3":
            print(f"{numero} x {i} = {numero * i}")
        elif opcao == "4":
            print(f"{numero} ÷ {i} = {numero / i:.2f}")
