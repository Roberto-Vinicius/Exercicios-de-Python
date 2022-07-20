salario = float(input('Qual sálario do funcionário?'))
if salario <= 1250:
    valor = salario * 15 / 100
    salario_atual = valor + salario
    print('Seu sálario atual é de:\033[1;31m{}R$'.format(salario_atual))
else:
    valor = salario * 10 / 100
    salario_atual = valor + salario
    print('Seu sálario atua é de:\033[1;32m{}R$'.format(salario_atual))
