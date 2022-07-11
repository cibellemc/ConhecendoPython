# receber 4 alunos e mostrar a ordem de apresentação

import random
alunos = []
count = 0

while count < 4:
    alunos.insert(count, input('{}° aluno: '.format(count)))
    count += 1

random.shuffle(alunos)
# não dá pra atribuir a uma nova variavel
print('Ordem de apresentação:', alunos)
