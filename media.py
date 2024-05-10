notas = []
for i in range(5):
    n = float(input(f"Insira a nota do {i+1}º aluno"))
    notas.append(n)

soma = 0
for i in range(5):
    soma += notas[i]

print(soma/len(notas))
