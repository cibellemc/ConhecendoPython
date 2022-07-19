# le 7 anos de nascimento e diz quantos sao maiores e menores (considerar 21)
from datetime import date
maiores = 0
menores = 0
atual = date.today().year

for c in range(1, 8):
    ano = int(input('{}° ano de nascimento: '.format(c)))
    if atual - ano >= 21:
        maiores += 1
    else:
        menores += 1

print('Há {} maior(es) de idade.\nHá {} menor(es) de idade.'.format(maiores, menores))
