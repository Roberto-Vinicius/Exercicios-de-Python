import random
a1 = input('qual o nome desse aluno?')
a2 = input('diga mais um?')
a3 = input('outro?')
a4 = input('mais um?')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print('o aluno sorteado foi:{}'.format(s))

