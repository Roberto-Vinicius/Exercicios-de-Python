from time import sleep
from random import randint
#listas e funções
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 1)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual sua jogada? '))

print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!')
#escolhas

    print('-=' * 15)
    print('Jogador jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[computador]))
    print('-=' * 15)
# funções SE
    if computador == 0: #JOGOU PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print("JOGADA INVALIDA")
    elif computador == 1: #JOGOU PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print("JOGADA INVALIDA")
    elif computador == 2: #JOGOU TESOURA
        if jogador == 0:
            print('JOGADOR VENCEU')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATOU')
        else:
            print("JOGADA INVALIDA")
