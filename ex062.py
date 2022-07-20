print('-='*9)
print('Termos de uma PA')
print('-='*9)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}-> '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostra agora? '))
print('Esse foi o total de termos {}.'.format(total))