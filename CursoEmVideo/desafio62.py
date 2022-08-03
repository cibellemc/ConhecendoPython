# melhorar o 61, perguntando ao final se quer continuar mostrando
termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
print(termo1, end=' ')

c = 1
while c < 10:
    termo = termo1 + razao
    print(termo, end=' ')
    termo1 = termo
    c += 1

continua = int(input('\nDeseja mostrar mais quantos termos? '))
while continua != 0:
    newC = c + continua
    while c < newC:
        termo = termo1 + razao
        print(termo, end=' ')
        termo1 = termo
        c += 1
    continua = int(input('\nDeseja mostrar mais quantos termos? '))
