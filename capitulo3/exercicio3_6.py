# Escreva uma expressão que será utilizada para decidir se um aluno
# foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser
# maiores ou iguais a 7. Considere que o aluno cursa apenas três matérias e que
# a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2
# e matéria3.

materia1 = int(input("Envie a primeiraa média: "))
materia2 = int(input("Envie a segunda média: "))
materia3 = int(input("Envie a terceira média: "))

if materia1 >= 7 and materia2 >= 7 and materia3 >= 7:
    print("O aluno etá aprovado")
else:
    print("O aluno esta reprovado")