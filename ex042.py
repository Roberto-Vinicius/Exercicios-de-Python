print('-='* 20)
print('Digite três seguimentos!!'.upper())
print('-='* 20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c: #if a == b ==c
        print('Formou um triagulo EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Formou um triagulo ISÓSCELES')
    elif a != b and a != c and b != c:  #elif a != b != c != a
        print('Formou um triangulo ESCALENO')
else:
    print('Os seguimentos NÃO podem formar um triangulo')
