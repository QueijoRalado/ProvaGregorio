import sys

# Lê a entrada inteira de uma vez
entrada = sys.stdin.read().splitlines()

numero_alunos = int(entrada[0])  # O primeiro valor é o número de alunos
lista_notas = []
lista_numero_alunos = []

# Começa a ler os dados dos alunos a partir da segunda linha
for i in range(1, numero_alunos + 1):
    informacoes_aluno = entrada[i].split()
    lista_numero_alunos.append(informacoes_aluno[0])
    lista_notas.append(int(informacoes_aluno[1]))

# Processa as notas
escolhido = "Minimum note not reached"
for n, nota in enumerate(lista_notas):
    if nota >= 8:
        escolhido = lista_numero_alunos[n]
        break

print(escolhido)