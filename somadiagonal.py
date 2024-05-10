m = []
for i in range(3):
    linha = []
    for i in range(3):
        n = int(input("Digite o número"))
        linha.append(n)
    m.append(linha)

soma = 0
for i in range(3):
    for j in range(3):
        if i == j:
            soma += m[i][j]

print(soma)
for x in m:
    print(x,"\n")
