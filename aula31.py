"""
Flag -> marcar um local
None -> sem valor
is | is not -> é ou não é
id -> identidade
"""

# v1 = 'a'
# print(id(v1))

condicao = True
passou_no_if = None

if condicao:
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if is None)