def voto(ano):
    from datetime import date
    media = date.today().year - ano
    print('--' * 10)
    print(f'sua idade é {media}')
    if media < 16:
        print('O voto NÃO é obrigatório')
    elif media >= 55:
        print('O voto opcional')
    else:
        print('O voto é OBRIGATÓRIO')
    return media


resp = (voto(int(input('Ano de nascimento: '))))
