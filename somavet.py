somavet = []
m = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite "))
        linha.append(n)
    m.append(linha)

for i in range(3):
    soma = 0
    for j in range(3):
        soma += m[j][i]
    somavet.append(soma)

for x in m:
    print(x,"\n")
print(somavet)
