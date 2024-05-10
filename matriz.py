m = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite"))
        linha.append(n)

    m.append(linha)

soma = 0
for i in range(3):
    for j in range(3):
        if j>i:
            soma += m[i][j]

for x in m:
    print(x,"\n")
print(soma)
