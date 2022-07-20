from time import sleep


def contador(a, b, c):
    if c < 0:
        c += -1
    if c == 0:
        c = 1
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(0.5)

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= c
        print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar')
contador(a=int(input('Início: ')), b=int(input('Fim: ')), c=int(input('Passo: ')))
