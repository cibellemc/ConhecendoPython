# 10 termos da PA

termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
print(termo1, end=' ')

# fórmula de PA => primeiro + (10 - 1) * razao
for c in range(1, 10):
    termo = termo1 + razao
    print(termo, end=' ')
    termo1 = termo
