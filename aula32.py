numero = input("Digite um número inteiro: ")

if numero.isdigit():
    if int(numero) % 2 == 0:
        print('Número é par')
    else:
        print('Número é ímpar')
else:
    print('Número digitado não é um inteiro')

""""""

horario = input('Que horas são: ')
horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11:
    print('Bom dia')
elif horario_int <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

""""""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Nome muito grande')