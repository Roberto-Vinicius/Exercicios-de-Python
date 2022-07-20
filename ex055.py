menor = 0
maior = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da pessoa {}:KG'.format(pessoa)))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior: #PARA ACHAR O MAIOR
            maior = peso
        if peso < menor: #PARA ACHAR O MENOR
            peso = menor
print('O MAIOR peso foi {:.2f} e o MENOR peso foi {:.2f}'.format(maior, menor))