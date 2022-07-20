expressão = str(input('Digite sua expressão: '))
pilha1 = []  #(
pilha2 = []  #)
for simb in expressão:
    if simb == '(':
        pilha1.append(simb)
    elif simb == ')':
        pilha2.append(simb)
if len(pilha1) == len(pilha2): #VERIFICADOR DE VALIDEZ
    print('Sua expressão é valida!')
else:
    print('Sua expressão NÃO é valida!')