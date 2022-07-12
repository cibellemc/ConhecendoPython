# começa com 'SANTO'

cidade = input('Cidade: ').strip()
cidade_splitada = cidade.split()
print(cidade_splitada[0].upper() == 'SANTO')

# outro modo: print(cidade(:5).upper() == 'SANTO')
