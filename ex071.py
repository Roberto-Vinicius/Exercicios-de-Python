print('\033[36m==\033[m'*20)
print('{:^40}'.format('BANCO TANGARÁ'))
print('\033[36m==\033[m'*20)
valor = int(input('Qual valor você que sacar? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break

