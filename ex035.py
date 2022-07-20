print('-='* 20)
print('Digite três seguimentos!!'.upper())
print('-='* 20)
a = float(input('Digite o primeiro seguimento:'))
b = float(input('Digite o segundo seguimento:'))
c = float(input('Digite o terceiro seguimento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM FORMAR um triangulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triangulo')