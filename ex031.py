viagem = float(input('Qual a distancia da sua viagem? km'))
print('Você está prestes a começar uma viagem de {}km'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('o preço da sua viagem ficou {:.2f}R$'.format(preço))

#OUTRA FORMA

