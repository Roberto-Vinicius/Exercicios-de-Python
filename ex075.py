valores = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
           int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Valores digitados {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'o valor 3 foi digitado na posição {valores.index(3) + 1}°')
else:
    print('o valor 3 não foi digitado nenhuma vez')
for c in valores:
    if c % 2 == 0:
        print(f'Esses foram os valores pares {c}')