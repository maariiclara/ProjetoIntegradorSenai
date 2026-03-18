# Toda a parte lógica do programa - funções

lista_alunos = []
# no proprio cadastro já vai fazer a verificação para evitar possiveis erros de notas 
# n aceita nota negativa ou maior que 10, e tbm n aceita menos de 2 notas para o aluno
def cadastro_aluno():
    print("** Cadastro de Aluno **")
    print("")
    nome = str(input("Qual o nome do aluno? "))
    qtd_notas = int(input(f"Quantas notas o(a) {nome} tem (precisa de no mínimo 2)? "))
    if qtd_notas < 2:
        print("** O sistema precisa de pelo menos 2 notas! **")
        return
    notas = []
    for i in range(qtd_notas):
        nota = float(input(f"Nota da Atividade {i+1}: "))
        while nota < 0 or nota > 10:
            print("   ** Nota inválida! Digite um valor entre 0 e 10! **")
            nota = float(input(f"Nota da Atividade {i+1}: "))
        notas.append(nota)
    aluno = (nome, notas)
    lista_alunos.append(aluno)
    print("")
    media = media_alunos(notas)
    print(f"** {nome} foi cadastrado(a) com sucesso! Com a média final de: {media:.2f} **")

