# le varios numeros, vai pergunatndo se quer parar e ao fim
# mostra menor e maior

num1 = int(input('Informe um valor: '))
opcao = input('Deseja continuar? [S/N]: ').upper()
maior = menor = soma = num1
qtd_num = 1

while opcao == 'S':
    qtd_num += 1
    num2 = int(input('Informe um valor: '))
    soma += num2
    if num2 > maior:
        maior = num2
    elif num2 < menor:
        menor = num2

    opcao = input('Deseja continuar? [S/N]: ').upper()

media = soma/qtd_num
print(f'Maior valor lido: {maior}\nMenor valor lido: {menor}')
print(f'A média dos {qtd_num} números digitados é {media:.1f}')
