from dados import contatos

data = contatos.fromkeys(["teste"], "testando")
print(data)

dados = contatos.items()
print(dados)

for i in dados:
    print(i)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))    

