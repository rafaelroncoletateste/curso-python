import os

palavraSecreta = 'arroz'
letrasCorretas = ''
numeroTentativas = 0

while True:
    letraDigitada = input('Digite uma letra: ')
    numeroTentativas += 1

    if len(letraDigitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letraDigitada in palavraSecreta:
        letrasCorretas += letraDigitada

    palavraFormada = ''

    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasCorretas:
            palavraFormada += letraSecreta
        else:
           palavraFormada = '*'

    print(f'Palavra formada: {palavraFormada}')

    if palavraFormada == palavraSecreta:
        os.system('cls')
        
        print('Você ganhou! Parabéns!')
        print(f'A palavra era {palavraSecreta}')
        print(f'Tentativas {numeroTentativas}')

        letrasCorretas = ''     
        numeroTentativas = 0