print('-='*9)
print('Termos de uma PA')
print('-='*9)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}-> '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM')
