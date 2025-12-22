"""
Iterando strings com while
"""

nome = 'Rafael'
contador = 0

tamanho_nome = len(nome)

while contador < tamanho_nome:
    print(f'*{nome[contador]}*')
    contador += 1