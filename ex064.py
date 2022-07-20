'''n = cont = tot = soma = soma_total = 0
while n != 999:
    n = int(input('Digite um número\033[31m[000 para parar]\033[m: '))
    cont = cont + 1
    soma = soma + n
    soma_total = soma - 999
    tot = cont - 1
print('Você digitou {} números e soma deles foi {}.'.format(tot, soma_total))'''

#OUTRA FORMA
n = cont = tot = soma = soma_total = 0
n = int(input('Digite um número\033[31m[000 para parar]\033[m: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número\033[31m[999 para parar]\033[m: '))
print('Você digitou {} números e soma deles foi {}.'.format(cont, soma))