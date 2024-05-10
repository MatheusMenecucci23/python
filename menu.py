print("Escolha a opção:")
print("1 - Soma de dois números:")
print("2 - Diferença de dois números")
print("3 - Produto de dois números")
print("4- Divisão de dois números")
op = int(input("Escolha um opção digitando seu numero"))
nOne = int(input("Digite o primeiro número"))
nTwo = int(input("Digite o segundo número"))
resp = 0
if(op == 1):
    resp = nOne + nTwo
elif(op == 2):
    if(nOne>nTwo):
        resp = nOne - nTwo
    else:
        resp = nTwo - nOne
elif(op == 3):
    resp = nOne * nTwo
elif(op==4):
    if(nTwo == 0):
        print("Não foi possível fazer a divisão por 0")
    else:
        resp = nOne/nTwo
else:
    print("Opção invalida")

print(resp)


