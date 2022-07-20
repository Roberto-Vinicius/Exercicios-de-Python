from random import randint
print('\033[31m-=\033[31m'*35)
print('O computador está pensando em um número entre 0 e 10, tente adivinhar')
print('\033[31m-=\033[m'*35)
pessoa = str(input('Qual sua escolha: '))
pc = randint(0, 10) #PARA O "PC" PENSAR EM UM NÚMERO ALEATÓRIO
cont = 1
while pessoa != pc:  #ATÉ ACERTAR A OPÇÃO DO PC
    pessoa = int(input('Qual sua escolha: '))
    cont = cont + 1
if pessoa == pc:
    print('Parabéns você ganhou!!')
    print('Você tentou {} vezes para acertar'.format(cont))
