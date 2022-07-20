from random import randint
cont = 0
print('=-'*13)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*13)
while True:
    jogador = int(input('Digite um valor: '))
    var = str(input('Par ou Ímpar[PAR/IMPAR]: ')).upper().strip()
    print('=-' * 13)
    pc = randint(1, 11)
    soma = pc + jogador
#VERIFICADOR DE PAR OU ÍMPAR
    if soma % 2 == 0: #PAR
        deu = 'PAR'
    else:  #IMPAR
        deu = 'IMPAR'
    print(f'Você jogou {jogador} e o pc {pc}. Total ficou {soma}, DEU {deu}')
#VERIFICADOR DE VITORIA
    if var == deu: #VENCEU
        print('--'*20)
        print('Você VENCEU!!')
        print('Vamos jogar novamente...')
        print('--' * 20)
    else:  #PERDEU
        print('--' * 20)
        print('você PERDEU')
        print('--' * 20)
        break
    cont = cont + 1
print(f'GAME OVER! Você venceu {cont} vezes')
