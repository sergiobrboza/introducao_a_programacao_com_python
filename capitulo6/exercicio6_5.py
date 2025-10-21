'''
Altere o programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente apenas um comando pode ser inserido por vez.Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS
'''
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("\nDigite:")
    print("F para adicionar cliente ao fim da fila")
    print("A para realizar atendimento")
    print("S para sair")

    operacoes = input("operações (F,A ou S): ").upper()

    for i in operacoes:
        if i == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia")
        elif i == "F":
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} adicionado ao fim da fila.")
        elif i == "S":
            print("Saindo do sistema...")
            exit()
        else:
            print("Operação inválida, tente novamente!")
