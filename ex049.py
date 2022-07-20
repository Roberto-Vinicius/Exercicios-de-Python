n = int(input('Digite um número para saber sua tabuada: '))
for c in range(1, 11):
    soma = n * c
    print('{} x {:2} = {}'.format(n, c, soma))
