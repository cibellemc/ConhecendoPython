# le ano e diz se tera que se alistar

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year

idade_atual = ano_atual - ano_nascimento

if idade_atual == 18:
    print('Esse ano você deve comparecer junto à Junta Militar para realizar alistamento.')
elif idade_atual < 18:
    espera = 18 - idade_atual
    ano_alistamento = date.today().year + espera
    print('Ainda não foi convocado para alistamento.')
    print('Seu alistamento será em {}. Aguarde mais {} ano(s).'.format(ano_alistamento,espera))
else:
    atraso = idade_atual - 18
    ano_alistamento = date.today().year - atraso
    print('Seu período de alistamento foi em {}, {} ano(s) atrás.'.format(ano_alistamento, atraso))
    print('Regularize-se junto à Junta Militar.')
