c = ('\033[m', #0 - sem cores
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;42m', #2 - verde
     '\033[0;30;44m', #3 - azul
     '\033[0;30;43m', #4 - amarelo
     '\033[7;30', #5 - branco
     '')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblíoteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
