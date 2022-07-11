# lê o comprimento do cateto oposto e do adjacente e calcula hipo
from math import hypot

cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('Hipotenusa:{:.2f}'.format(hipotenusa))