# calcula prestação mensal do emprestimo, que não pode exceder 30% do salario
# le valor da casa, salario e em quantos anos vai pagar

print('{} BANCO POPULAR {}'.center(70, '-').format('\033[1;34m', '\033[m'))
print('Para concessão de empréstimo precisaremos de algumas informações:')

valor_casa = float(input('1) Valor da casa a ser comprada: R$'))
salario = float(input('2) Valor do seu salário: R$'))
anos = int(input('3) Em quantos anos deseja pagar: '))

meses = anos * 12
prestacao = valor_casa / meses

if salario <= 0 or meses <= 0:
    print('\nNão é possível calcular sua prestação. Insira valores válidos.')
else:
    if prestacao > salario * 30 / 100:
        print('\nEmpréstimo {}negado{}'.format('\033[1;31m', '\033[m'))
        print('O valor da prestação excede seu orçamento.')
    else:
        print('\nEmpréstimo {}aprovado{}.'.format('\033[1;32m', '\033[m'))
    print('O valor da prestação será de R${:.2f}.'.format(prestacao, meses))
