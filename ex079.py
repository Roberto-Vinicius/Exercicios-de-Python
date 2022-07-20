lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n) #PARA ADICIONAR ITENS NA LISTA
        print('Valor adicionado...')
    else:
        print('Valor já existente, NÃO foi adicionado...')
    resp = ' '  #MECANISMO DE PARADA
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(f'os números digitados ficaram assim {lista}')