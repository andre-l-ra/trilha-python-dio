# Tuplas são como listas, porém imutáveis

tpl = tuple([1,2,6]) # Declarando uma tupla com uma lista de inteiros
print(tpl)

print(f"O numere 6 está na posição.: ", tpl.index(6)) # Mostra o indice pelo elemento

matriz = ((1, 2, 3), (4,5,6), (7,8,9),)

print(f"Na posição 1x1 da matriz está o número.: {matriz[1][1]}")

carros = ("gol")
print(isinstance(carros, tuple))