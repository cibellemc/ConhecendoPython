# le um valor e informa como sera pagamento

valor = float(input('Valor do produto: R$'))
print('\nOpcões de pagamento: ')
print('[1] - Dinheiro ou Cheque')
print('[2] - Débito')
print('[3] - 2x no cartão')
print('[4] - 3x ou mais no cartão\n')

condicao_pagamento = float(input('Forma de pagamento desejada: '))
av_dinheiro = valor - (valor * 10 / 100)
av_cartao = valor - (valor * 5 / 100)
cartao_3x = valor + (valor * 20 / 100)

if condicao_pagamento == 1:
    print('Valor a pagar: R${:.2f} com desconto'.format(av_dinheiro))
elif condicao_pagamento == 2:
    print('Valor a pagar: {:.2f} com desconto'.format(av_cartao))
elif condicao_pagamento == 3:
    parcela = valor / 2
    print('Valor da prestação: R${:.2f}, em 2x sem juros'.format(parcela))
    print('Valor total da compra: R${:.2f}'.format(valor))
elif condicao_pagamento == 4:
    vezes = int(input('Em quantas vezes deseja dividir? '))
    parcela = cartao_3x / vezes
    print('Valor da prestação: R${:.2f}, em {}x com juros'.format(parcela, vezes))
    print('Valor total da compra: R${:.2f}'.format(cartao_3x))
else:
    print('Opção de pagamento inválida.')
