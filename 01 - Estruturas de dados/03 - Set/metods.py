conjunto_a = {1,3,5}

conjunto_b = {1,3,2,4,6}

# uniao: faz a junção dos dois conjuntos
uniao = conjunto_a.union(conjunto_b)
intersec = conjunto_a.intersection(conjunto_b)
diference_ab = conjunto_a.difference(conjunto_b)
diference_ba = conjunto_b.difference(conjunto_a)
print(f"A união dos conuntos é.: {uniao}")
print(f"A intersecção dos conuntos é.: {intersec}")
print(f"A diferença entre a e b é.: {diference_ab}")
print(f"A diferença entre b e a é.: {diference_ba}")
