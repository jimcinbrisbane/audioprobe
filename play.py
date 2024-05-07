#play audio
#update pip
#pip3 install pygame
import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load('./recording1.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

play()

