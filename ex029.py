velocidade = float(input('Qual a veocidade atual do carro?'))
if velocidade > 80:
    print('---MULTADO---\nVocê ultrapassou o limite de velocidade que é de 80km/h' )
    multa = (velocidade-80) * 7
    print('A sua multa ficou em {}R$'.format(multa))
print('Tenha um bom dia! Dirija com segurança!!')

