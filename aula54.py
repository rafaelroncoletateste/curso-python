import os

lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[I]nserir [A]pagar [L]istar: ')

    # INSERIR
    if opcao == 'i' or opcao == 'I':
        os.system('cls')

        valor = input('Valor: ')
        lista.append(valor)

    # APAGAR
    elif opcao == 'a' or opcao == 'A':
        os.system('cls')

        indice_str = input('De qual índice você deseja apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except: # É altamente recomendado tratar o erro especificamente (ex: ValueError, TypeError etc)
            print('Não foi possível apagar esse índice')

    # LISTAR
    elif opcao == 'l' or opcao == 'L':
        os.system('cls')

        if len(lista) == 0:
            print('Não existe itens para listar')
            continue

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor digite um caractere válido')