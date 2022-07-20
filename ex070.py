soma = cont = menor = mais_mil = 0
barato = ''
while True:
    print('{:-^40}'.format('\033[35mCALCULADORA DE PRODUTOS\033[m'))
    nome = str(input('Qual o nome do produto: '))
    preço = float(input('Qual o preço do produto: R$'))
    cont = cont + 1
    if cont == 1 or preço < menor:  #NOME DO PRODUTO MAIS BARATO
        menor = preço
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma = soma + preço #SOMA OS PREÇOS DOS PRODUTOS
    if preço > 1000:  #PRODUTOS ACIMA DE 1000 REAIS
        mais_mil = mais_mil + 1
    if continuar == 'N':
        break
print(f'Essa foi a soma da sua compra R${soma}')
print(f'{mais_mil} produtos custam mais que R$1000')
print(f'Produto mais barato foi {barato.upper()} e custa R${menor}')
