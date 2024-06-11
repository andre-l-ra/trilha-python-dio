# Remove a primeira ocorrencia do elemento pelo nome

linguagens = ["c#", "c++", "ruby", "python", "c#", "js", "dart"]

linguagens.remove("c#") # Remove a primeira ocorrencia de c#
print(linguagens)

for lang in linguagens:
    if lang == "c#":
        linguagens.remove(lang)

print(linguagens)