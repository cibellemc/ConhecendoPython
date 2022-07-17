# le duas notas e diz se ta aprovado, reprovado ou recuperação

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

print('Média: {:.1f}'.format(media))
if media >= 7:
    print('Parabéns! Você está {}aprovado{}!'.format('\033[1;32m', '\033[m'))
elif media < 5:
    print('Você está {}reprovado{}!'.format('\033[1;31m', '\033[m'))
else:
    print('Estude mais! Você está em {}recuperação{}!'.format('\033[1;33m', '\033[m'))

