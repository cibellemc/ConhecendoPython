# le 4 nomes e sorteia um
import random
alunos = []
count = 0

while count < 4:
    alunos.insert(count, input('{}° aluno: '.format(count)))
    count += 1

aluno_sorteado = random.randint(0,3)

print('\nSorteado para apagar o quadro: {}'.format(alunos[aluno_sorteado]))

# outra forma

import random
alunos = []
count = 0

while count < 4:
    alunos.insert(count, input('{}° aluno: '.format(count)))
    count += 1

aluno_sorteado = random.choice(alunos)

print('\nSorteado para apagar o quadro: {}'.format(aluno_sorteado))