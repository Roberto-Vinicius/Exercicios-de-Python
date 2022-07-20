num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c),end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num, tot))
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número NÃO é primo')

