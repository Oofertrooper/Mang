import pygame
import time
import sys
pygame.init()

ekraan = pygame.display.set_mode([400, 600])
mäng_töötab = True
ekraan.fill([133, 193, 233])
taust = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Taust_päev.png")
ekraan.blit(taust, (0, 0))

pygame.display.flip()
while mäng_töötab:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()