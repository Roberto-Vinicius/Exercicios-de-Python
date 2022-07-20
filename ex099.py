from time import sleep


def maior(*valores):
    print('-='*20)
    print('Analisando os valores passados...')
    print(f'{valores} Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')
    sleep(1)


#programa principal
maior(1, 5, 3, 4)
maior(3, 7, 0)
maior(1, 2)
