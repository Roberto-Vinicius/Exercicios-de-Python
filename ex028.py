import random
from time import sleep
'''pessoa = int(input('Tente adivinha qual vai ser o número que o pc vai escolher, de 1 a 5:'))
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n0, n1, n2, n3, n4, n5]
pc = random.choice(lista)
if pessoa != pc:
    print('Você perdeu! -- Eu pensei no número {}'.format(pc))
else:
    print('Você ganhou, PÁRABENS!')'''

#OUTRA FORMA DE RESPOSTA
pessoa = int(input('Tente adivinha qual vai ser o número que o pc vai escolher, de 0 a 5:'))
computador = random.randint(0, 5)
print('PROCESSANDO...')
sleep (3)
if pessoa != computador:
    print('Você perdeu! -- Eu pensei no número {}'.format(computador))
else:
    print('Você ganhou, PÁRABENS!')