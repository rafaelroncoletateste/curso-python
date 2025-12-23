while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ | - | / | *)')

    sair = sair.lower()

    numeros_validos = None
    operadores_permitidos = '+-/*'

    try:
        num1_float = float(num1)
        num2_float = float(num2)

        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos')
        continue

    if operador not in operadores_permitidos or len(operador) > 1:
        print('Operador inválido')
        continue
    
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    else:
        print('Você')

    sair = input('Quer sair da calculadora? [S]im')

    if sair == 's':
        break