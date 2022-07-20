from datetime import date
ano = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(0, 7):
    nome = int(input('Em que ano você {} nasceu: '.format(pessoa +1)))
    idade = ano - nome
    if idade > 18: # MENORES
        total_maior += 1
    else: # MAIORES
        total_menor += 1
print('Tivemos {} MENORES DE IDADE e {} MAIORES DE IDADE'.format(total_menor, total_maior))

