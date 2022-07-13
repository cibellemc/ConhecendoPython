# bissexto
ano = int(input('Ano a ser analisado: '))
# divisivel por 4, exceto divisivel por 100 e nao divisivel por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')
