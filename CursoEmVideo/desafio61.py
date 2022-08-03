termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
print(termo1, end=' ')
c = 1

# fórmula de PA => primeiro + (10 - 1) * razao
while c < 10:
    termo = termo1 + razao
    print(termo, end=' ')
    termo1 = termo
    c += 1
