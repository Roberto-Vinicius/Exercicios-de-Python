frase = str(input('digite uma frase:')).strip().lower()
print('a letra A aparece:{}'.format(frase.count('a')))
print('a primeira letra A aparece na posição:{}'.format(frase.find('a')+1))
print('a ultima letra A aparece na posição:{}'.format(frase.rfind('a')+1))