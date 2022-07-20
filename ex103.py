def jogador(nome, num):
    if nome.strip() == '':
        print('O jogador desconhecido fez', end=' ')
    else:
        print(f'O jogador {nome} fez', end=' ')
    if num.isnumeric():
        num = int(num)
    else:
        num = 0
    print(f'{num} gol(s) no campeonato.')


jogador(str(input('Nome do Jogador: ')), str(input('Número de Gols: ')))
