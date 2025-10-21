'''
Modifique o programa para trabalhar com duas filas para facilitar seu trabalho considere o comando A para atendimento da fila 1; B, para atendimento da fila 2. O mesmo para a chegada dos clientes: F para fila1; e G para fila2.
'''
ultimo1 = 10
fila1 = list(range(1, ultimo1 + 1))
ultimo2 = 10
fila2 = list(range(1, ultimo2 + 1))

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1.")
    print(f"Fila 1 atual: {fila1}")
    print(f"\nExistem {len(fila2)} clientes na fila 2.")
    print(f"Fila 2 atual: {fila2}")
    print("\nDigite:")
    print("F para adicionar cliente ao fim da fila 1")
    print("G para adicionar cliente ao fim da fila 2")
    print("A para realizar atendimento da fila 1")
    print("B para realizar atendimento da fila 2")
    print("S para sair")

    operacoes = input("operações (F, G, A, B ou S): ").upper()

    for i in operacoes:
        if i == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia")
        elif i == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia")
        elif i == "F":
            ultimo1 += 1
            fila1.append(ultimo1)
            print(f"Cliente {ultimo1} adicionado ao fim da fila.")
        elif i == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
            print(f"Cliente {ultimo2} adicionado ao fim da fila.")
        elif i == "S":
            print(f"Resultado fila 1: {fila1}")
            print(f"Resultado fila 2: {fila2}")
            print("Saindo do sistema...")
            exit()
        else:
            print("Operação inválida, tente novamente!")
