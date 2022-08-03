# fatorial

numero = int(input('Digite um número: '))
num = numero
fatorial = numero

while num - 1 > 0:
    antecessor = num - 1
    fatorial *= antecessor
    num = antecessor

print(f'{numero}! = {fatorial}')

# factorial(n)
# fazer com contador, ir multiplicando e decrementando