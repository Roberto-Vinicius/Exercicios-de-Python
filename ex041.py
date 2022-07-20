from datetime import date
atleta = int(input('Qual seu ano de nascimento?'))
ano = date.today().year #ANO ATUAL
idade = ano - atleta #CALCULLAR IDADE
if idade <= 9:
    print('Você tem {} anos, isso te encaixa na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, isso te encaixa na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, isso te encaixa na categoria JUVENIL'.format(idade))
elif idade <= 20:
    print('Você tem {} anos, isso te encaixa na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos, isso te encaixa na categoria MASTER'.format(idade))
print('PARABÉNS!! agora você é um atl1eta da confederação nacional de natação')