# condição de existencia de um triangulo
# cada lado deve ser menor que a soma dos outros 2

lado1 = float(input('1° lado: '))
lado2 = float(input('2° lado: '))
lado3 = float(input('3° lado: '))

if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print('Formam triângulo.')
else:
    print('Não formam triângulo.')

