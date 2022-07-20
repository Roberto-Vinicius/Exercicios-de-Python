mais_velho = 0
maioridade = 0
homenvelho = 0
cont = 0
for c in range(1, 5):
    print('---- {}° PESSOA ----'.format(c))  #FORMULÁRIOS
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()
#HOMEN MAIS VELHO
    if c == 1 and sexo == 'M':
        maioridade = idade
        homenvelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        homenvelho = nome
#MULHER COM MENOS DE 20
    if sexo == 'F' and idade < 20:
        cont += +1
media = idade / 4
print('A média de idade desse grupo foi {}'.format(media))
print('O HOMEN mais velho tem {} anos e se chama {}'.format(maioridade, homenvelho))
print('Tem {} mulheres com menos de 20 anos.'.format(cont))