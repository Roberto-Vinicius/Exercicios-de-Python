from random import randint


def soma(num):
    r = 0
    for p, n in enumerate(num):
        if n % 2 == 0:
            r += n
    print(f'Sorteando 5 valores da lista: {num}')
    print(f'Somando os valores pares de {num} temos: {r}')


#Principal
lista = list()
for c in range(0, 5):
    v = randint(1, 10)
    lista.append(v)
soma(lista[:])
