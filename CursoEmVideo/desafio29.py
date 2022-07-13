#le velocidade e diz se é multado
velocidade = int(input('Velocidade do carro (km/h): '))

if velocidade > 80:
    print('Multa por excesso de velocidade!')
    multa = (velocidade - 80) * 7
    print('Valor a pagar: R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida!')
