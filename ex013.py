s = float(input('qual seu sálario atual?R$'))
p = s * 15 / 100
n = s + p
print('seu sálario era de R${:.2f}, mas com o aumento de 15% ficou em {:.2f}'.format(s, n))