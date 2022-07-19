# le nome, idade, sexo de 4 pessoas
# diz a media de idade, nome do homem mais velho e qts mulheres < 20

mulheres = 0
idade_velho = 0
nome_velho = ''

print('----- 1° pessoa ----- ')
nome = input('Nome: ').strip()
sexo = input('Sexo (F/M): ').strip().upper()
idade = int(input('Idade: '))

soma = idade
if sexo == 'M':
    idade_velho = idade
    nome_velho = nome
elif sexo == 'F':
    if idade < 20:
        mulheres += 1

for c in range(2, 5):
    print('----- {}° pessoa ----- '.format(c))
    nome = input('Nome: ').strip()
    sexo = input('Sexo (F/M): ').strip().upper()
    idade = int(input('Idade: '))

    soma += idade

    if sexo == 'm'.upper():
        if idade > idade_velho:
            nome_velho = nome
            idade_velho = idade
    elif sexo == 'F'.upper():
        if idade < 20:
            mulheres += 1

media = soma / 4

print('\nMédia de idade do grupo: {}'.format(media))
if idade_velho != 0:
    print('{} é o homem mais velho. Ele tem {} anos'.format(nome_velho, idade_velho))
print('Há {} mulhere(s) com menos de 20 anos'.format(mulheres))
