# informar categoria na natacao
# ate 9 mirim, ate 14 infant, ate 19 junior ate 20 senior, acima master

from datetime import date
print('{}--- Categoria Esportiva ---{}'.format('\033[1;34m', '\033[m'))
ano_nasc = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano_nasc
print('Idade:', idade)
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
