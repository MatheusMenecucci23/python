""" 3) (5 pontos) Faça um programa que receba do usuário o nome de um arquivo
texto. Crie outro arquivo texto contendo o conteúdo do arquivo de entrada,
mas com as vogais substituídas por * """

n = input("escreva o nome do arquivo")
f = open(n,"r")
s = f.readlines()
f.close()
s_modi = ""
for j in range(len(s)):
    for i in range(len(s[j])):
        if s[j][i] in "AEIOUaeiou":
            s_modi += "*"
        else:
            s_modi += s[j][i]

out = open("text.txt", "w+")
for i in range(len(s_modi)):
    out.write(s_modi[i])
out.close() 
print(s_modi)


















        
