# pedra papel tesoura
from time import sleep
from random import randint
pc = randint(0, 2)

itens = ['PEDRA', 'PAPEL', 'TESOURA']
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
jogador = int(input('>'))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)

print('-' * 30)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))

# dentro de cada bloco há 3 possibilidades para o jogador
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    if jogador == 1:
        print('Jogador VENCEU!')
    if jogador == 2:
        print('Jogador PERDEU!')
elif pc == 1:
    if jogador == 0:
        print('Jogador PERDEU!')
    if jogador == 1:
        print('EMPATE!')
    if jogador == 2:
        print('Jogador VENCEU!')
elif pc == 2:
    if jogador == 0:
        print('Jogador VENCEU!')
    if jogador == 1:
        print('Jogador PERDEU!')
    if jogador == 2:
        print('EMPATE!')
