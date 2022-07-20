lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SsNn':  #MECANISMO DE PARADA
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*10)
lista.sort()
lista.reverse()
print(f'Foram digitados {len(lista)} valores')
print(f'Os valores da lista ficaram assim {lista} em ordem decrescente')
if 5 in lista:
    print('O 5 foi digitado e está na lista')
else:
    print('O 5 não foi digitado e não está na lista')
    