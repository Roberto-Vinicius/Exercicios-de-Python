dados = dict()
gols = list()
cont = 0
dados['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for g in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {g}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'o jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'   => Na partida {i}, fez {v}')
print(sum(gols))
