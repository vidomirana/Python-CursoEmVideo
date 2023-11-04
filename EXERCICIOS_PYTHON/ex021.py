# Reproduzir um arquivo em mp3
import pygame

pygame.init()  # iniciar o módulo pygame
pygame.mixer.music.load('ex021.mp3')  # carregar o arquivo mp3
pygame.mixer.music.play()  # tocar o arquivo mp3
input()
pygame.event.wait()  # esperar a música acabar pra parar
