# adivinhar numero que o computador esta pensando

from random import randint
from time import sleep
# dá um tempo de pausa

numero_pc = randint(0, 1)

print('-- JOGO DE ADIVINHAÇÃO --')
numero_user = int(input('Que número estou pensando? '))
print('Analisando...')
sleep(2)

if numero_pc != numero_user:
    print('Você perdeu! Eu pensei no número {}.'.format(numero_pc))
else:
    print('Você venceu!!')
