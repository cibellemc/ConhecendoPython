# fibonacci

num = int(input('Quantos elementos deseja exibir? '))
print('0 1', end=' ')
c = 3
antecessor = 0
sucessor = 1

while c <= num:
    f = antecessor + sucessor
    print(f, end=' ')
    antecessor = sucessor
    sucessor = f
    c += 1
