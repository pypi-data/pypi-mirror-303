import pygame

pygame.mixer.init()
success_sound = pygame.mixer.Sound('./sound/3beeps-108353.mp3')

def play_success_sound():
    success_sound.play()
