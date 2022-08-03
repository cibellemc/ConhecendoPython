# le dois valores, mostra menu e realiza operação
def menu():
    print('\nEscolha uma opção:')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair')


num1 = float(input('1° valor: '))
num2 = float(input('2° valor: '))

menu()
opcao = int(input('> '))

while opcao != 5:
    if opcao == 1:
        print('Soma =', num2+num1)
    elif opcao == 2:
        print('Multiplicação =', num2*num1)
    elif opcao == 3:
        if num2 > num1:
            print('O maior é', num2)
        else:
            print('O maior é', num1)
    elif opcao == 4:
        num1 = float(input('1° valor: '))
        num2 = float(input('2° valor: '))
        menu()
    else:
        print('Opção inválida.')
    opcao = int(input('> '))
