import random
a1 = str(input('diga um nome?'))
a2 = str(input('diga outro nome?'))
a3 = str(input('outro?'))
a4 = str(input('só mais um?'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem será')
print(lista)
