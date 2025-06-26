'''Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.'''
numero = int(input("Digite um número: "))

if numero < 2:
    print("Não é primo")
elif numero == 2:
    print("É primo")
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
    print("É primo" if eh_primo else "Não é primo")
