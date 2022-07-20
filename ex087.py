lista = [[], [], []]
pares = maior = 0
for c in range(0, 9):
    valores = int(input('Digite um valor para a matriz: '))
    if valores % 2 == 0: #VALORES PARES
        pares += valores
    if c < 3:
        lista[0].append(valores)
    if 2 < c <= 5:
        lista[1].append(valores)
    if 5 < c <= 9:
        lista[2].append(valores)
lista_0 = lista[0]
lista_1 = lista[1]
lista_2 = lista[2]
soma = lista_0[2] + lista_1[2] + lista_2[2] #SOMA DOS VALORES DA TERCEIRA COLUNA
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print(f'A soma de todos os valores pares ficou {pares}')
print(f'A soma dos valores da terceira coluna foi {soma}')
print(f'O maior valor da segunda linha é {max(lista_1)}')
