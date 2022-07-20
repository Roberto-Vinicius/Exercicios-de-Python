import math
a = float(input('digite uma angulo:'))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('o cosseno desse angulo é {:.2f}'.format(c))
print('o seno desse angulo é {:.2f}'.format(s))
print('a tangente desse angulo é {:.2f}'.format(t))