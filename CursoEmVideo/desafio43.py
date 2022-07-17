# imc = peso(kg) / alutura(metros )**2

peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))

imc = peso / altura ** 2
print('IMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida')
