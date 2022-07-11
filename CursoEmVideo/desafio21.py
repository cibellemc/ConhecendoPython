# abrir e reproduzir um áudio MP3
# reproduz sem erro com apenas uma barra mas fica aparecendo aviso aviso do PyCharm

from playsound import playsound
playsound("C:\\ConhecendoPython\\CursoEmVideo\\piano.mp3")

"""""
-- quando não especifica o caminho todo reproduz mas para e dá erro 

Error 263 for command:
        close piano.mp3
    O dispositivo especificado não está aberto ou o MCI não o reconhece.
Failed to close the file: piano.mp3

-- colocando um input vazio depois do music.play não para execução
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('piano.mp3')
pygame.mixer.music.play()
pygame.event.wait()"""""