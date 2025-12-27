for i in range(10):
    if i == 2:
        print('I é 2, pulando...')
        continue

    if i == 8:
        print('I é 8, (parar)')
        break

    print(i)
else:
    print('For completo com sucesso!')