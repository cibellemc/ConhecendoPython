# leia de 0 a 9999 e mostre cada numero separado (und, dez, cen)
num = int(input('Numero: '))

milhar = num // 1000
centena = num // 100 % 10
dezena = num // 10 % 10
# 4321 // 10 = 432 % 10 = 432 / 10 = 43 (resto 2)
# meu modo de pensar: deze = (num % 100) // 10
unidade = num % 10
# 4321 % 10 = 4321/10 = 432 (resto 1)

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))

# se fosse como string era so pegar o num[0],num[1] etc (nem precisa de split)