# lê nome completo, mostra em upper e lower, o tamanho splitado e quantas letras tem o primeiro nome

# coloca um strip logo no inicio p/ garantir que não havera espaco desnecessario
nome = (input('Nome completo: ')).strip()
print(nome.upper())
print(nome.lower())

# vê o tamanho e subtrai a quantidade de espaços em branco
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))

nome_splitado = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome_splitado[0])))

# outro modo de fazer é usando nome.find(' '): vai mostrar o numero onde cortou a primeira vez
