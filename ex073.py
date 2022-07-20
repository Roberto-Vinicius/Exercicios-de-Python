cont = 0
cont2 = 16
times = ('América-MG', 'Athletico-PR','Atlético-GO', 'Atlético-MG','Avaí',
         'Botafogo', 'Ceará SC','Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
         'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print('~~'*20)
for primeiros in times[0:5]:
    cont = cont + 1
    print(f'Esse é o {cont}° colocado: {primeiros}')
print('~~'*20)
for ultimos in times[16:]:
    cont2 = cont2 + 1
    print(f'Esse é o {cont2}° colocado: {ultimos}')
print('~~'*20)
for ordem in sorted(times):
    print(f'Colocação em ordem alfabética: {ordem}')
print('~~'*20)
for pos, nome in enumerate(times):
    if pos == 10:
        print(f'O {nome} está na {pos}° colocação')
