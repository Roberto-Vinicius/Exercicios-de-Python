from math import factorial
num = int(input('Digite um número para ver seu fatorial: '))
print('Número escolhido: {}!'.format(num))
for c in range(num, 0, -1):
    print(end='{}'.format(c))
    print(' x 'if c > 1 else ' = ', end='')
print(factorial(num))