numero_alunos = 0
lista_notas = []
lista_numero_alunos = []
n = 0
escolhido = "Minimum note not reached"

while numero_alunos<3:
    numero_alunos = int(input("numero de alunos (minimo 3): "))

print(numero_alunos)
for numero in range(0, numero_alunos):
    informacoes_aluno = str(input("escreve as coisa aí: "))
    n=0
    for coisas in informacoes_aluno.split():
        n+=1
        if n==1:
            lista_numero_alunos.append(coisas)
        if n==2:
            lista_notas.append(coisas)
n=0

lista_notas2 = list(map(int, lista_notas))

for nota in lista_notas2:
    if nota>=8:
        escolhido = lista_numero_alunos[n]
        break
    n+=1

print(escolhido)