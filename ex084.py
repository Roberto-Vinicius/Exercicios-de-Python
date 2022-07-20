pessoas = list()
cadastrados = list()
maior = menor = 0
while True:
    cadastrados.append(str(input('Qual o seu nome? ')))
    cadastrados.append(float(input('Qual o seu peso: KG ')))
    if len(cadastrados) == 0:
        maior = menor = cadastrados[1]
    else:
        if cadastrados[1] > maior:
            maior = cadastrados[1]
        if cadastrados[1] < maior:
            menor = cadastrados[1]

    pessoas.append(cadastrados[:])
    cadastrados.clear()# APAGA LISTA ANTERIOR

    resp = ' '  #MECANISMO DE PARADA
    while resp not in 'NnSs':
       resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'e foi de {p[0]}\n')
print(f'o menor peso foi {menor}', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'e foi de {p[0]}')