print('=====LOJAS DANTAS=====')
preço = float(input('Qual o preço do produto?R$ '))
print('''Escolha a forma de pagamento:
[1] Dinheiro ou pix: 10% de desconto  
[2] 2X no cartão: Preço normal
[3] Á vista no cartão: 5% de desconto
[4] 3X ou mais no cartão: 20% de juros''')
opçao = int(input('Qual sua opção: '))
if opçao == 1:
    desconto = preço - (preço * 10 / 100)
    print('O preço do seu produto foi de {:.2f} R$, mas com o desconto ficou {:.2f} R$'.format(preço, desconto))
elif opçao == 2:
    print('Sua compra ficou {:.2f} R$'.format(preço))
elif opçao == 3:
    desconto = preço - (preço * 5 / 100)
    print('O preço do seu produto foi de {:.2f} R$, mas com o desconto ficou {:.2f} R$'.format(preço, desconto))
elif opçao == 4:
    parcelas = int(input('Quantas parcelas? '))
    preço_atual = (preço * 20 / 100) + preço
    pp = preço_atual / parcelas
    print('O preço do seu produto foi de {:.2f} R$, mas com os juros ficou {:.2f} R$ \nSerá parcelado em {} de {:.2f}'.format(preço, preço_atual, parcelas,pp ))
else:
    print('Não exixte essa opção')
print('OBRIGADO PELA COMPRA!!')
