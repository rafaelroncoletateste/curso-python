"""
split - Divide uuma string
join - Une uma string
strip - Corta os espaços (existe também: rstrip, lstrip)
"""

frase = 'Hello World!  Teste '
lista_palavras = frase.split('!')

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

print(lista_palavras)