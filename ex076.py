listagem = ('Lápis', 1.25,
            'Caderno', 10,
            'Apontador', 2,
            'Estojo', 5.50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${listagem[pos]:<5.2f}')