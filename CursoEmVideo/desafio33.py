num1 = float(input('Num 1: '))
num2 = float(input('Num 3: '))
num3 = float(input('Num 3: '))
# outra forma é admitir um como maior e menor
if num1 > num2:
    maior = num1
    menor = num2
    if maior < num3:
        maior = num3
    if menor > num3:
        menor = num3
else:
    maior = num2
    menor = num1
    if maior < num3:
        maior = num3
    if num3 < num1:
        menor = num3

print('O maior é', maior)
print('O menor é', menor)
