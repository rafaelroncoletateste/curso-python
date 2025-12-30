nomes = 'Rafael', 'Gabriel', 'Vitor'

lista_enumerada = enumerate(nomes)
print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)

for indice, nome in lista_enumerada: # Aqui retorna o indice e o valor referente ao indice
    print(indice, nome)