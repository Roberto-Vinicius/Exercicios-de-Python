var = cont = 0
soma = quant = media = 0
maior = menor = 0
while var != 'N':
#CONTADOR
    cont = cont + 1
    num = int(input('Digite um número: '))
    soma = soma + num
#RESPOSTA
    var = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#MEDIA
    media = soma / cont
#MAIOR VALOR
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} números, a média ficou {:.2f}, o maior número foi {} e o menor foi {}'.format(cont, media, maior, menor))
