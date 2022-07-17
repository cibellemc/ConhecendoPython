# aperfeiçoando desafio 35
# dizer se é equilátero, escaleno ou iso

lado1 = float(input('1° lado: '))
lado2 = float(input('2° lado: '))
lado3 = float(input('3° lado: '))

if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print('É um triângulo!')

# pode ser tambem lado1 == lado2 == lado3
    if lado1 == lado2 and lado3 == lado2:
        print('Tipo do triângulo: Equilátero')
    elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
        print('Tipo do triângulo: Isósceles')
    else:
        print('Tipo do triângulo: Escaleno')

else:
    print('Não é um triângulo.')

