sexo = str(input('Seu SEXO é [M/F]: ')).upper()
#M = 'M'
#F = 'F'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Essa opção não é valida, digite novamente: ')).upper()
if sexo == 'M':
    print('Seu sexo é MASCULINO!')
elif sexo == 'F':
    print('Seu sexo é FEMININO!')