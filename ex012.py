p = float(input('qual o preço do produto? R$'))
n = p * 5 / 100
d = p - n

print('O novo preço com o desconto de 5% é {:.2f}'.format(d))