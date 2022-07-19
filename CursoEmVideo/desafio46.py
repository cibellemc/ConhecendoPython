# contagem regressiva de 10  a 0 com 1 seg de pausa

from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize("FELIZ ANO NOVO!! :fogos_de_artifício:", language='pt'))
