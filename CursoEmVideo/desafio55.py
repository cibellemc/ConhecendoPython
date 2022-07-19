# le o peso de 5 pessoas, diz maior e menor

peso = float(input('1° peso: '))
maior = peso
menor = peso

for c in range(2, 6):
    peso = float(input('{}° peso: '.format(c)))

    if peso >= maior:
        maior = peso
    else:
        if peso <= menor:
            menor = peso
print('Maior peso: {:.1f}kg\nMenor peso: {:.1f}kg'.format(maior, menor))
