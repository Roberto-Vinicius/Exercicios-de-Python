while True:
    n = int(input('Digite um número para ver sua tabuada\033[32m[Digite um valor negativo para encerrar]\033[m: '))
    print('\033[31m==\033[m'*20)
    if n < 1: #MECANISMO DE PARADA
        break
    for c in range(1, 11): #TABUADA
        tab = c * n
        print(f'{n:2} x {c:2} = {tab:2}')
    print('\033[31m==\033[m' * 20)
print('OBRIGADO POR USAR MEU PROGRAMA')
