contador = 0

while contador <= 10:
    contador += 1

    if contador == 4:
        print('não mostrarei o', contador)
        continue

    print(contador)

print('Acabou')