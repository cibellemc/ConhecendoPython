# le salario e caucula aumento
# > 1250 aumenta 10% < aumenta 15%

salario = float(input('Salário atual: R$'))
if salario > 1250:
    novosalario = salario + (salario * 0.10)
else:
    novosalario = salario + (salario * 0.15)

print('Novo salário: R${:.2f}'.format(novosalario))
