string = input("Digite uma palavra")
c = 0
qtd = 0
for i in string:
    if i == "a":
        c+=1
    elif i == "e":
        c+=1
    elif i == "i":
        c+=1
    elif i == "o":
        c+=1
    elif i == "u":
        c+=1

    if i in "aeiouAEIOU":
        qtd = qtd + 1

print(c)
print(qtd)

