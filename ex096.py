
def area(largura, altura):
    area = largura * altura
    print(f'A área de um de terreno {largura:.2f} x {altura:.2f} é de {area}m.')


print('-----------CONTROLE DE TERRENO----------')
print('=='*20)
area(float(input('LARGURA (m): ')), float(input('ALTURA (m): ')))
