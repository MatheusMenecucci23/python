m = []
for i in range(3):
    linha = []
    for i in range(3):
        n = int(input("Digite o número"))
        linha.append(n)

    m.append(linha)
c = 0
for i in range(3):
    for j in range(3):
        if m[i][j] > 10:
            c +=1

print(c)
