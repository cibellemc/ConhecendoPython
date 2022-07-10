# carro custa 60 po dia e 0.15 por km
dias_aluguel = int(input('Quantos dias alugado? '))
km_rodados =  float(input('Quantos km rodados? '))
valor_aluguel = (60 * dias_aluguel) + (0.15 * km_rodados)
print('O total a pagar é de R${:.2f}'.format(valor_aluguel))
