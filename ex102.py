print('CACULADOR E FATORIAL')


def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = fatorial(int(input('Digite um número: ')), True)
print(n)