def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de varios aluno.
    :param n: uma ou mais notas de vários alunos (aceita várias).
    :param sit: valor opcional, mostra a situação do aluno se está BOA, RAZOÁVEL ou RUIM.
    :return: um dicionario com a situação da turma
    Criado por Roberto Vinicius
    """
    r = dict()
    r['total'] = len(n)
    r['maxima'] = max(n)
    r['mínima'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] <= 5:
            r['Situação'] = 'RUIM'
        elif 5 > r['média'] < 7:
            r['Situação'] = 'RAZOÁVEl'
        else:
            r['Situação'] = 'BOA'
    return r


#PROJETO PRINCIPAL
resp = notas(6.5, 0, 8, sit=True)
print(resp)
