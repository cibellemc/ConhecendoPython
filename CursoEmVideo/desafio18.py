# lê um ângulo e mostra sen, cos e tg
import math

angulo = float(input('Informe um ângulo: '))

# converte o angulo pra radianos e dps calcula o seno
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno,cosseno,tangente))
