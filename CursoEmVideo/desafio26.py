# le frase mostra quantas vezes aparece a, em que posicao aparece a primeira e a ultima
frase = input('Digite uma frase: ').strip().upper()
# da um upper na hora do recebimento
# nesse caso, os espaços irão alterar a posição

print('Há {} letras A'.format(frase.count('A')))
print('Primeira ocorrência de A: {}° posição'.format(frase.find('A')))

# rfind procura da direita praa esquerda
print('Última ocorrência de A: {}° posição'.format(frase.rfind('A')))

