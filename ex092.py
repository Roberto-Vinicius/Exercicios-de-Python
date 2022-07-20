from datetime import date

atual = date.today()
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados["ctps"] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Sálario: R$'))
    dados['idade'] = atual.year - nascimento
    a = dados['ano de contratação'] + 35
    dados['Aposentadori'] = (a - atual.year) + dados['idade']
print('-='*20)
for k, v in dados.items():
    print(f' - {k}: {v}')
