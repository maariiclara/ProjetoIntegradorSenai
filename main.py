from processamento import * # já vai importar todos os defs do processamento

print("*********** SISTEMA DO DESEMPENHO ACADÊMICO - SENAI ***********")

while True:
    print("")
    print("*********** Escolha Uma Opção: **********")
    print("* 1. Cadastrar Aluno e Nota             *")
    print("* 2. Lista Completa dos Alunos          *")
    print("* 3. Alunos em Recuperação              *")
    print("* 4. Aluno(a) em Destaque               *")
    print("* 5. Gerar Relatório                    *")
    print("* 6. Sair do Sistema                    *")
    print("*****************************************")
    print("")

    escolha = int(input("Escolha o número desejado: "))

    if escolha == 1:
        cadastro_aluno()
    elif escolha == 2:
        todos_alunos(lista_alunos)
    elif escolha == 3:
        pass
    elif escolha == 4:
        pass
    elif escolha == 5:
        pass
    elif escolha == 6:
        pass
    else:
        print("** Opção inválida! Tente novamente! **")