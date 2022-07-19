# tabuada com for

num = int(input('Número: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))
    c = c + 1
