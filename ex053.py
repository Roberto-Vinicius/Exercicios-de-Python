frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # outra maneira sem o laço
'''inverso = ''# MANEIRA COM O LAÇO
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase NÃO é um palíndromo.')