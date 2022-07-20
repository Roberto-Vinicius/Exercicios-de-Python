print('\033[1;33;44m--- ESCREVA NÚMEROS INTEIROS ---\033[m')
num_1 = int(input('Escreva o primeiro: '))
num_2 = int(input('Escreva o segundo: '))
if num_1 > num_2:
    print('O primeiro valor {} é MAIOR.'.format(num_1))
elif num_2 > num_1:
    print('O segundo valor {} é MAIOR.'.format(num_2))
else:
    print('Não exite valor maior os dois são iguais')
print('\033[1;33;44m--- OBRIGADO ---\033[m')