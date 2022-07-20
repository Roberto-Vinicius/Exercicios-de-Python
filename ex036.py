valor_casa = float(input('Qual o valor da casa?R$'))
salario = float(input('Qual seu sálario?R$'))
anos = int(input('Em quantos anos você vai pagar?R$'))
parcela = (valor_casa / anos) / 12
porcentagem = salario * 30 / 100
if parcela > porcentagem:
    print('Desculpa, você não pode comprar essa casa')
else:
    print('PARABÉNS, você pode comprar essa casa, o valor da parcela ficou em {:.2f}R$'.format(parcela))
print('Obrigado pelo contato.')
