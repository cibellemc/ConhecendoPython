# soma dos impares multiplos de 3 entre 1 e 500

soma = 0

for c in range(3, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('Soma: {}'.format(soma))
