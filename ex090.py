aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média igual a {aluno["media"]}')
print('-='*10)
if aluno["media"] >= 7:
    print('Situação igual: APROVADO')
elif aluno["media"] <= 5:
    print('Situação igual: REPROVADO')
else:
    print('Situação igual: RECUPERAÇÃO')
    