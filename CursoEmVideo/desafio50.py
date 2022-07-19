# le 6  numeros soma os pares

soma = 0

for c in range(1, 7):
    num = int(input('{}° número: '.format(c)))
    if num % 2 == 0:
        soma += num

print('A soma é: {}'.format(soma))
