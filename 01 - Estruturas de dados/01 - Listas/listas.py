letras = list("python")
numeros = list(range(10))
linguage = "python"
cores = ["laranja", "azul", "preto"]

print(letras)
print(numeros)
print(linguage[::-1]) #inverte a string

for index, cor in enumerate(cores):
    print(f"{index}: {cor}")

#compreenssao de listas
pares = []
sqrt = [numero ** 2 for numero in numeros]

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
print(sqrt)

#métodos

## Append
pares.append(10)
print(pares)

## Copy
copia_pares = pares.copy
print(id(pares) , " : " , id(copia_pares))

## Clear
pares.clear()
print(pares)

lista_com_repeticoes = [1, 2, 3, 1, 4, 5, 1]
print(lista_com_repeticoes.count(1)) #conta quantas vezes o elemento 1 aparece na lista

# Extend (junta duas listas)
# Não exclui itens repetidos

linguagens = ["python", "js", "java"]
linguagens2 = ["c#", "c++", "ruby", "python"]

linguagens.extend(linguagens2)
print(linguagens)