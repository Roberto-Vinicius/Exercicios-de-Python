lista_final = [[], []]
for c in range(1, 8):
    valores = int(input(f'Digite seu {c}° valor: '))
    if valores % 2 == 0:
        lista_final[0].append(valores)
    else:
        lista_final[1].append(valores)
lista_final[0].sort()
lista_final[1].sort()
print('\033[31m-=\033[m'*30)
print(f'Esse foram os valores pares digitados {lista_final[0]}')
print(f'Esses foram os valores impares digitados {lista_final[1]}')