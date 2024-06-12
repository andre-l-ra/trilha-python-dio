declaracao_1 = {"Nome" : "Andre", "Idade" : 34}

declaracao_2 = dict(Nome="Andre", Idade=34)
print(declaracao_2)

declaracao_2["Telefone"] = "997799721"
print(declaracao_2)

# Lendo valores
print(f"Olá {declaracao_2['Nome']}, você tem {declaracao_2['Idade']} anos de idade")

# Dicionarios Aninhados
contatos = {
    "teste1@test.com" : dict(Nome="teste1", Telefone="111111111"),
    "teste2@test.com" : dict(Nome="teste2", Telefone="222222222"),
    "teste3@test.com" : dict(Nome="teste3", Telefone=dict(Residencial="33333333333", Trabalho="777777777"))
}
print(contatos['teste3@test.com']['Telefone']['Trabalho'])

# Interando o dict

#metodo 1
for chave in contatos:
    print(chave, contatos[chave])

#metodo 2 (recomendado)
for chave, valor in contatos.items():
    print(chave, valor)
