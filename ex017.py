'''import math
o = float(input('qual o comprimento do cateto oposto?'))
a = float(input('qual o comprimento do cateto adjacente?'))
s = a**2 + o**2
h = math.sqrt(s)
print('a hipotenusa dessa soma é {:.2f}'.format(h))'''

#segundo metodo
import math
o = float(input('qual o comprimento do cateto oposto?'))
a = float(input('qual o comprimento do cateto adjacente?'))
h = math.hypot(o, a)
print('a hipotenusa é {:.2f}'.format(h))
