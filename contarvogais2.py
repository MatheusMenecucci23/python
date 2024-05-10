c = 0
word = input("Digite")
for i in range(len(word)):
    if word[i] in "aeiouAEIOU":
        c += 1


print(c)
