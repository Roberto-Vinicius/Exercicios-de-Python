from random import randint
from operator import itemgetter
jogo = {'jogador 1': randint(0, 6), 'jogador 2': randint(0, 6),
        'jogador 3': randint(0, 6), 'jogador 4': randint(0, 6)}
ranking = list()
print(f'-===-Valores sorteados-===-')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'-==-RANKING DOS JOGADORES-==-')
for i, v in enumerate(ranking):
    print(f'  {i + 1} lugar: {v[0]} com {v[1]}')