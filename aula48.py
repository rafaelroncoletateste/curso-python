# append -  Adiciona um item no final
# insert - Adiciona no índice escolhido
# pop - Remove do final ou do índice escolhido
# del - Apaga um índice
# clear - Limpa a lista
# extend - Estende a lista


# string = 'ABCDE'

# # lista = list()

# outraLista = ['a', 'b']
# lista = [123, 'Rafael', 1.23, outraLista]
# print(lista)

# listaNumeros = [10, 20, 30 ,40]
# del listaNumeros[3]
# print(listaNumeros)

# listaNumeros.append(50) # Adiciona ao final da lista
# listaNumeros.pop() # Remove o último elemento da lista

listaNumeros = [10, 20, 30 ,40]
ultimoItem = listaNumeros.pop()
listaNumeros.insert(0, 1200)

print(ultimoItem)