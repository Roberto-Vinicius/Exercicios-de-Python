print('\033[1;31;46m=-\033[m'* 12)
print('Digite alguns valores!!'.upper())
print('\033[1;31;46m=-\033[m'* 12)
v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
v3 = int(input('Terceiro valor:'))
#verificação do menor
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
#verificador do maior
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O menor valor foi: {}'.format(menor))
print('O maior valor foi: {}'.format(maior))
