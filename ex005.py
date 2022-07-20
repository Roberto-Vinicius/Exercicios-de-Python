n = int(input('Digite um número:'))
a = int(n - 1)
s = int(n + 1)

print ('analisandoo valor {}, seu antescessor é {}, e seu sucessor é {}'.format(n , a, s))

#segunda forma de resolução

n = int(input('digite um número:'))
print('analisandoo valor {},seu antescessor é {}, e seu sucessor é {}'.format(n, n+1, n-1))