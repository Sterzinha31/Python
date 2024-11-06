# solicita os 5 números aos usuários
alunos = []
notas = []

for i in range (5):
    aluno = input("\nDigite o nome do aluno(a): ")
    nota = int(input("Digite a NOTA do aluno(a): "))
    alunos.append(aluno)
    notas.append(nota)

for i in range(5):
    print(f"O(a) aluno(a) {alunos[i]} tirou nota {notas[i]}")    