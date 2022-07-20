print('CALCULADORA DE MÉDIA')
nota_1 = float(input('Diga uma nota: '))
nota_2 = float(input('Diga outra: '))
media = (nota_1 + nota_2) / 2
if media < 5.0:
    print('Sua média ficou {}, você foi \033[0;0;31mREPROVADO\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média ficou {}, você ficou em \033[0;0;34mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua média ficou {}, você foi \033[0;0;32mAPROVADO\033[m'.format(media))
print('\033[0;33;40mCONHECIMENTO ABRE PORTAS\033[m')