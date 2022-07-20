print('DIGITE DOIS NÚMEROS')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('''Escolha uma opção no nosso MENU:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR  DO PROGRAMA''')
escolha = int(input('>>>>QUAL SUA ESCOLHA: '))
while escolha != 5:
    if escolha == 4:  #PARA USAR NOVOS NÚMEROS
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        escolha = int(input('>>>>QUAL SUA ESCOLHA do MENU: '))
    else:
        if escolha == 1: #PARA SOMAR
            soma = num1 + num2
            print('\033[31m-=\033[m' * 20)
            print('O resultado da sua SOMA foi {}.'.format(soma))
        elif escolha == 2:  #PARA MULTIPLICAÇÃO
            multiplicação = num1 * num2
            print('\033[31m-=\033[m' * 20)
            print('O resultado da sua MULTIPLICAÇÃO FOI {}.'.format(multiplicação))
        elif escolha == 3:  #PARA ACHAR O MAIOR
            if num1 > num2:
                print('\033[31m-=\033[m' * 20)
                print('O MAIOR número é {}.'.format(num1))
            else:
                print('\033[31m-=\033[m' * 20)
                print('O MAIOR número é {}.'.format(num2))
        elif escolha > 5:
            print('\033[31m-=\033[m' * 20)
            print('OPÇÃO INVALIDA, tente novamente.')
        print('\033[31m-=\033[m' * 20)
        print('''
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA   ''')
        escolha = int(input('>>>>QUAL SUA ESCOLHA: '))
        print('\033[31m-=\033[m' * 20)
print('obrigado por usar nossos serviços')
print('\033[31m-=\033[m' * 20)