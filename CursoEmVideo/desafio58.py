from random import randint
from time import sleep

print('Jogo da adivinhação')
print('-*' * 18)
print('Tente acertar o número em que pensei!')

qtd_tentativas = 1
pc = randint(0, 10)
user = int(input('> '))

while user != pc:
    print('Processando....')
    sleep(0.5)
    print(f'\033[31mVocê errou!!\033[m Eu pensei no número {pc}')
    print('Tente de novo.')

    qtd_tentativas += 1
    pc = randint(0, 10)
    user = int(input('> '))

print('Processando....')
sleep(0.5)
print('\033[32mParabéns!!\033[m')
print(f'Depois de {qtd_tentativas} tentativa(s) você conseguiu vencer.')
