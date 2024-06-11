# Ordena lista 

langs = ["c#", "c", "ruby", "python", "javascript", "php", "swift", "scala", "kotlin"]
langs.sort() # Ordena por ordem alfabética

print(langs)
print(ord)

langs.sort(reverse= True) # Ordena de forma reversa
print(langs)

langs.sort(key= lambda x : len(x))
print(langs)

langs.sort(key= lambda x : len(x), reverse= True)
print(langs)

a = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(a)