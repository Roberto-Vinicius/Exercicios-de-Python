lista = [[], [], []]
for c in range(0, 9):
    valores = int(input('Digite um valor para a matriz: '))
    if c < 3:
        lista[0].append(valores)
    if 2 < c <= 5:
        lista[1].append(valores)
    if 5 < c <= 9:
        lista[2].append(valores)
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
