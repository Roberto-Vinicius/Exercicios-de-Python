valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*10)
maior = max(valores)
menor = min(valores)
for posição, valor in enumerate(valores):
    if valor == maior:
        print(f'O maior valor foi {maior} e está na posição {posição}')
        print('--'*10)
    if valor == menor:
        print(f'O menor valor foi {menor} e está na posição {posição}')
        print('--' * 10)