print('\033[31m-=\033[m'* 11)
print('SEQUÊNCIA DE FIBONACCI')
print('\033[31m-=\033[m'* 11)
n = int(input('Quantos termos você quer mostrar: '))
print('\033[31m~~\033[m'* 18)
t1 = 0
t2 = 1
print('{} -> {} ->'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' {} ->'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' FIM')
