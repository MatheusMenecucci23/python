km = int (input("digite o km"))
qtd = int (input("digite o qtd gasolina"))
consumo = km/qtd
if (consumo < 8):
    print("Venda o carro")
elif(consumo < 12):
    print("economico")
else:
    print("supereconomico")
