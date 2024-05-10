"""(6 pontos) Faça um programa no qual o usuário informa o nome do
arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo. """
n = "palavras.txt"
f = open(n,"r")
word = input("digite a palavra:")
word += "\n"
s = f.readlines()
c = 0
print(s)
for i in range(len(s)):
    if s[i] == word:
        c +=1
        
print(c)  
