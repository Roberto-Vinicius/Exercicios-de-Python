cont = homens = mulheres = pessoas_cadastradas = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo[M/F]: ')).upper().strip()[0]
    print('~~'* 15)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    print('~~'*15)
    if idade > 18: #MENORES DE 18
        cont = cont + 1
    if sexo == 'M': #CONTADOR DE HOMENS
        homens = homens + 1
    if sexo == 'F' and idade <= 20: #CONTADOR DE MULHERES
        mulheres = mulheres + 1
    pessoas_cadastradas += 1
    if continuar == 'N':
        break
print(f'Foram cadastradas {pessoas_cadastradas} dessas,\n{cont} pessoas tem MAIS de 18 anos,')
print(f'{homens} pessoas do sexo MASCULINO cadastradas\n{mulheres} pessoas do sexo FEMININO e com MENOS de 20 anos cadastradas')
