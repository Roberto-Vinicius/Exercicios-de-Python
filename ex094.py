pessoa = dict()
galera = list()

soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de é {soma / len(galera)} anos')
print(f'As mulheres cadastratadas foram', end=' ')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end='')
print()
print('-='*20)
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= soma / len(galera):
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<<DEPRESSÃO>>>')
