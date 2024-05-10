"""Escreva uma função que receba um número inteiro positivo Ne em
seguida imprima N linhas do chamado Triangulo de Floyd. Para N = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21 """

def floyd(n):
    num = 1
    for i in range(1,n+1):
        word = ""
        for j in range(i):
            word += str(num) + " "
            num +=1
        print(word)

n = int(input("digite o número: "))
floyd(n)




