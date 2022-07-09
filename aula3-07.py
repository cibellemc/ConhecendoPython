# area e qt de tinta usa (cada litro pinta 2m quadrado)
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura*altura
qtd_tinta = area/2
print('Área: {:.2f} metros quadrados\nSerá necessário {:.2f} litros de tinta para pintar a parede'.format(area, qtd_tinta))
