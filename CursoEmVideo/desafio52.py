# primo

numero = int(input('Digite um número: '))

for c in range(2, numero):
    if numero % c == 0:
        print('Não é primo.')
        break
    else:
        print('É primo!')
        break

# outro jeito é contar a qtd de vezes q dividiu, se for > 2 não é primo
