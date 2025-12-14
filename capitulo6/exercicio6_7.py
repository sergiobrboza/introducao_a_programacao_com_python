'''
Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:

Código
(())  Ok
()()()()) Ok
()) Erro

Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.
'''

def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False 
            else:
                pilha.pop()

    return len(pilha) == 0

expressoes_para_testar = [
    ("(()())", "OK"),
    ("()()()", "OK"),
    ("())", "Erro"),
    ("((()", "Erro"),
    (")(", "Erro"),
    ("((a + b) * c)", "OK (ignora letras)")
]

for exp, resultado_esperado in expressoes_para_testar:
    status = "OK" if verifica_parenteses(exp) else "Erro"
    print(f"Expressão: '{exp}' | Resultado: {status} | Esperado: {resultado_esperado}")