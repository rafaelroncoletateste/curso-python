"""
in -> Entre
not in -> Não está entre
"""

nome = input('Digite o seu nome: ')

if 'a' or 'A' in nome:
    print("Tem a letra 'a' no nome") 
else:
    print("Não tem a letra 'a' no nome")