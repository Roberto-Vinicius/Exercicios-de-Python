ficha = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])

    #MECANISMO DE PARADA
    resposta = ' '
    while resposta not in 'SsNn':
        print('\033[31m--\033[m'*15)
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        print('\033[31m--\033[m'*15)
    if resposta == 'N':
        break

print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')