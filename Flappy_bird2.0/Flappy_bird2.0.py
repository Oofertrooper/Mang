import pygame
import time
import sys
pygame.init()

pygame.display.set_caption("Flappy")
icon = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind1.png")
pygame.display.set_icon(icon)
mäng_töötab = True


ekraan = pygame.display.set_mode(([2000, 1000]), pygame.WINDOWMAXIMIZED)
ekraan.fill([133, 193, 233])
taust = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Taust_õhtu.png")
taust = pygame.transform.smoothscale(taust, ekraan.get_size())
ekraan.blit(taust, (0, 0))

lind1 = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind1.png")
lind2 = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind2.png")
lind1 = pygame.transform.scale(lind1, (300, 300))
ekraan.blit(lind1, (500, 300))


pygame.display.flip()
while mäng_töötab:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()