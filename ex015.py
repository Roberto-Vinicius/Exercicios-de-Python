d = int(input('quantos dias você ficou com o carro?'))
k = float(input('quantos quilometros você rodou com ele?'))
dia = d * 60
km = k * 0.15
preço = dia + km

print('você tem que pagar {} R$ pelo aluguel do carro.'.format(preço))