# pede distancia, calcula 50 centavos por km em viagens ate 200
# calcula 0,45 por viagens mais longas

distancia = int(input('Distância da viagem: '))
if distancia > 200:
    pagamento = 0.45 * distancia
else:
    pagamento = 0.50 * distancia

print('Valor a pagar: R${:.2f}'.format(pagamento))