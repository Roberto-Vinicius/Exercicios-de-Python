from datetime import date
sexo = str(input('Qual seu sexo? ')).lower().strip()
if sexo == 'masculino':
        ano = int(input('Qual foi seu ano de nascimento? '))
        idade = date.today().year - ano
        if idade < 18: #AINDA É CEDO
            print('você ainda tem {} anos, Bolsonaro ainda não te quer!!'.format(idade))
            falta = 18 - idade
            print('Falta {} para o seu chamado'.format(falta))
        elif idade == 18:  #O TEMPO É AGORA
            print('Você tem {} anos, Bolsonaro está chamando!!'.format(idade))
        elif idade > 18:  #JA PASSOU DO TEMPO
            print('Você tem {} anos, Bolsonaro te chamou e você não ouviu!!'.format(idade))
            passou = idade - 18
            print('Bolsonaro te chama a {} anos e você não ouve!!'.format(passou))
else:
    print('Você não precisa se alistar')
print('\033[1;31;46m-- OBRIGADO POR COMPARECER --\033[m')
