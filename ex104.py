def leiaInt(num):
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mERRO! Digite apenas números\033[m')
    return num


#projeto principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
