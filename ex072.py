cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO','SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
        'QUINZE', 'DEZESSEIS', 'DEZESSETE',
        'DEZOITE', 'DEZENOVE', 'VINTE')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente noamente', end='. ')
for pos, nome in enumerate(cont):
    if pos == num:
        print(f'O numero que você digitou foi o {nome}')