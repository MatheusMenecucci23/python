""" 1) (6 pontos) Faça duas funções, uma recursiva e outra Iterativa As funções
devem receber como parámetro um inteiro Ne retornar o resultado da
seguinte série
s = 1/1 + 3/2+5/3+ 2n-1/n
"""
"""def calculo(n):
    s = 0
    for i in range(1,n+1):
        s += ((2*i)-1)/i
    print(s)

n = int(input('Digite o número'))
calculo(n)"""


def calculo(n, i=1, s=0):
    if i > n:
        print(s)
        return
    s += ((2*i)-1)/i
    calculo(n, i+1, s)


n = int(input('Digite o número'))
calculo(n)




