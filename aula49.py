"""
Cuidados com dados mutáveis
    = - copia o valor
    = - aponta para o  mesmo valor na memória
"""

lista_a = ['Rafael', 'Gabriel']
lista_b = lista_a.copy() # Faz uma cópia da lista

lista_a[0] = 'Aleatório'
print(lista_b)