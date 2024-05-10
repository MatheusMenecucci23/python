string = input("Digite uma palavra: ")
palavra = ""
for i in range(len(string)-1,-1,-1):
    palavra = palavra + string[i]

palavra2 = string[len(string)-1::-1]
print(palavra)
print(palavra2)


palavrasub = string[:3]
palavrasub1 = string[1:3]
palavrasub2 = string[1:]

print(palavrasub)
print(palavrasub1)
print(palavrasub2)



