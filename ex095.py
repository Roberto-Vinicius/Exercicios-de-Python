dados = dict()
gols = list()
jogadores = list()
cont = 0
while True:
    gols.clear()
    dados['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    for g in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {g + 1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'cod   nome       gols      total')
for c, j in enumerate(jogadores):
    print(c, end=' -->')
    for k, v in j.items():
        if k == 'nome':
            print(f' {v} -->', end=' ')
        if k == 'gols':
            print(f' {v} -->', end=' ')
        if k == 'total':
            print(f' {v}')
print('--'*20)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para Parar) '))
    for c, v in enumerate(jogadores):
        if resp == c:
            for k, d in v.items():
                if k == 'nome':
                    print(f'--LEVANTAMENTO DO JOGADOR {d}')
                if k == 'total':
                    print(f'Jogou {cont + 1} jogos e acumulou {d} gols')
                    cont += 1
    if resp == 999:
        break
print('Não volte sempre')
