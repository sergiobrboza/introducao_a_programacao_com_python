'''Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.'''
while True:
    print("\nEscolha uma operação:")
    print("A - Adição")
    print("B - Subtração")
    print("C - Sair")

    escolha = input("Digite a letra da opção desejada: ").lower()

    if escolha == "a":
        print("Você escolheu adição.")
    elif escolha == "b":
        print("Você escolheu subtração.")
    elif escolha == "c":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
