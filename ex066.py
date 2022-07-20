soma = cont = 0
while True:
    n = int(input('Digite um número[999 faz parar]: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Você digitou {cont} números e a soma foi {soma}.')