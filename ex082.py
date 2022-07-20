completa = []
par = []
impar = []
while True:
    valores = int(input('Digite um valor: '))  #OBTENDO VALORES
    completa.append(valores)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if valores % 2 == 0:  # VALORES PARES
        par.append(valores)
    else:  #VALORES IMPARES
        impar.append(valores)
    if resp == 'N':
        break
print(f'A lista com todos os valores ficou assim {completa}')
print(f'Esses são os valores PARES digitados {par}')
print(f'Esse são os valores IMPARES digitados {impar}')