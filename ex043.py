peso = float(input('Qual seu peso:KG '))
altura = float(input('Qual sua altura:M '))
imc = peso / altura ** 2
if imc < 18.5:
    print('IMC = {:.1f}, você está ABAIXO do peso ideal.'.format(imc))
elif 18.5 > imc < 25:
    print('IMC = {:.1f}, você está no peso IDEAL'.format(imc))
elif 25 >= imc < 30:
    print('IMC = {:.1f}, você está com SOBREPESO'.format(imc))
elif 30 >= imc < 40:
    print('IMC = {:.1f}, você está com OBESIDADE'.format(imc))
else:
    print('IMC = {:.1f}, você está com OBESIDADE MÓRBIDA'.format(imc))
print('SAÚDE É O QUE INTERESSA!!')