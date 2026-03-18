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


def media_alunos(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


def todos_alunos(lista_alunos):
    maior_media = aluno_destaque(lista_alunos)
    print("** Lista Completa dos Alunos **")
    print("")
    for nome, notas in lista_alunos:
        media = media_alunos(notas)
        print(f"* {nome} - Média: {media:.2f}")
        if media < 7:
            print("Aluno(a) em Recuperação")
            print("")
        elif media == maior_media:
            print("Aluno(a) Top Student")
            print("")
        else:
            print("Aluno(a) Aprovado")
            print("")


def alunos_recuperacao(lista_alunos):
    print("** Alunos em Recuperação **")
    print("")
    for nome, notas in lista_alunos:
        media = media_alunos(notas)
        if media < 7:
            print(f"* {nome} - Média: {media:.2f}")
            print("")


def aluno_destaque(lista_alunos):
    maior_media = 0
    melhor_aluno = ""
    for nome, notas in lista_alunos:
        media = media_alunos(notas)
        if media > maior_media:
            maior_media = media
            melhor_aluno = nome
    return melhor_aluno, maior_media


def gerar_relatorio(lista_alunos):
    arquivo = open("resultado.txt", "w", encoding="utf-8")
    arquivo.write("******** RELATÓRIO DE DESEMPENHO ******** \n")
 
    melhor_aluno, maior_media = aluno_destaque(lista_alunos)
    for nome, notas in lista_alunos:
        media = media_alunos(notas)
        arquivo.write(f"\n* {nome} - Média: {media:.2f} \n")
        if media < 7:
            arquivo.write("Aluno(a) em Recuperação \n")
        else:
            arquivo.write("Aluno(a) Aprovado \n")   
    arquivo.write(f"\nTOP STUDENT: {melhor_aluno} - Média: {maior_media:.2f}")
    arquivo.close()