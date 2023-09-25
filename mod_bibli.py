alunos = {}  # Dicionário de alunos (matrícula: nome)

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} com matrícula {matricula} adicionado.")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} com matrícula {matricula} removido.")
    else:
        print("Aluno não encontrado.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = nome
        print(f"Nome do aluno com matrícula {matricula} atualizado para {nome}.")
    else:
        print("Aluno não encontrado.")

def VerAlunos():
    print("Lista de Alunos:")
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula}, Nome: {nome}")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Atualizar Aluno")
    print("4. Ver Alunos")
    print("5. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        AdicionarAluno()
    elif opcao == "2":
        RemoverAluno()
    elif opcao == "3":
        AtualizarAluno()
    elif opcao == "4":
        VerAlunos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
