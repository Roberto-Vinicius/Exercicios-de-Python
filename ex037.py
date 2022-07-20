num = int(input('Escreva um nùmero inteiro: '))
print('''Escolha uma das bases de conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO ficou {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL ficou {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL ficou {}'.format(num, hex(num)[2:]))
else:
    print('ESSA NÃO É UMA OPÇÃO')