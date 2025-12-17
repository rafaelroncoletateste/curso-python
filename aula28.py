nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Desculpa você deixou campos vazios')

nome_invertido = nome[::-1]
print(nome_invertido)

nome_contem_espaco = ' ' in nome
if nome_contem_espaco:
    print('Seu nome contém espaço')
else:
    print('Seu nome não contém espaço')

print(len(nome))
print(nome[0])
print(nome[-1])
