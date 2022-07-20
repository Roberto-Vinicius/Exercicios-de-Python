import math
num = float(input('digite uma numero:'))
r = math.trunc(num)
print('o número {} tem a parte inteira {}.'.format(num, r))

#segunda forma
from math import trunc
num = float(input('digite uma numero:'))

print('o número {} tem a parte inteira {}.'.format(num, trunc(num)))