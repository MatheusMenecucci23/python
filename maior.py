m = []
for i in range(5):
    n = int(input("Digite o número"))
    m.append(n)

maior = 0
for i in range(5):
    if i == 0:
        maior = m[i]
    if maior < m[i]:
        maior = m[i]

print(maior)
            
