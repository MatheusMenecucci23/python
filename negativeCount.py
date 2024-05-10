m = []
for i in range(10):
    n = int(input(f"Digite o {i+1}º número"))
    m.append(n)

c = 0
soma = 0
for i in range(10):
    if m[i] <0:
        c +=1
    else:
        soma += m[i]

print("Soma: ", soma, "Quantidade negativos: ",c)
