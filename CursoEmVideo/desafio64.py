# le varios inteiros ate flag 999. somar tds os outros anteriores

num = int(input('1° número: '))
c = 2
soma = 0
if num != 999:
    while num != 999:
        soma += num
        num = int(input(f'{c}° número: '))
        c += 1
print('Soma dos números diferentes de 999:', soma)