print('-='*9)
print('Termos de uma PA')
print('-='*9)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + 1, razao):
    print((c), end=' ->')
print('ACABOU')