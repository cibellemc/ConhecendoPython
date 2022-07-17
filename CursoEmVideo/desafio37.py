# le um inteiro e converte p binario(1), octal(2), hexa (3)

# 1) https://www.youtube.com/watch?v=Q9roAKKH9WA&t=140s

print('Conversor de bases'.center(30, '-'))
numero = int(input('Número para converter: '))
print('1 - Converter para binário')
print('2 - Converter para octal')
print('3 - Converter para hexadecimal')
opcao = int(input('> '))

binario = ''
octal = ''
hexa = ''

# 2) método da própria linguagem, pega de 2 p/ frente porque
# começa com 0 e a inicial da base. ex 0b111
if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])

if opcao == 1:
    while numero > 1:
        divisao = numero // 2
        binario += str(numero % 2)
        numero = divisao
    # sempre termina em 1
    binario += '1'
    # [::-1] inverte a string
    print(binario[::-1])
elif opcao == 2:
    while numero > 0:
        divisao = numero // 8
        octal += str(numero % 8)
        numero = divisao
    print(octal[::-1])
elif opcao == 3:
    # dicionario de conversao
    dic = {1: '1', 2: '2', 3: '3', 4: '4',
           5: '5', 6: '6', 7: '7', 8: '8',
           9: '9', 10: 'A', 11: 'B', 12: 'C',
           13: 'D', 14: 'E', 15: 'F'}
    while numero != 0:
        divisao = numero % 16
        # o resto da divisao transformado pra letra
        hexa = hexa + dic[divisao]
        numero = numero // 16
    print(hexa[::-1])
else:
    print('Opção inválida. Escolha [1], [2] ou [3]')

