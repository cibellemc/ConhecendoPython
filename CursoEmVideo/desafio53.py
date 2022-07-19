# le frase e diz se é palíndromo

frase = input('Frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

"""""for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""""
if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é palíndromo.')


"""""for c in range(0, len(frase)):
    if frase[c] != frase[inverso - 1]:
        print('Não é palíndromo.')
        break
    else:
        print('É palíndromo')
        break"""""
