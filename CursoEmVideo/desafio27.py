# mostra nome e ultimo sobrenome
nome = input('Nome completo: ').strip()
fatia_nome = nome.split()
primeiro = fatia_nome[0]
ultimo = fatia_nome[len(fatia_nome) - 1]
print('Primeiro nome: {}\nUltimo nome: {}'.format(primeiro, ultimo))
