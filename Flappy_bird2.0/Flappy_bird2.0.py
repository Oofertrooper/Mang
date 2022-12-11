import pygame
import time
import sys
pygame.init()
clock = pygame.time.Clock()
#Aken
pygame.display.set_caption("Flappy")
icon = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind1.png")
pygame.display.set_icon(icon)
mäng_töötab = True

#Pildid
ekraan = pygame.display.set_mode(([2000, 1000]), pygame.WINDOWMAXIMIZED)
ekraan.fill([133, 193, 233])
taust = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Taust_õhtu.png")
taust = pygame.transform.smoothscale(taust, ekraan.get_size())
ekraan.blit(taust, (0, 0))
nimi_y = 300
nimi = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Flappy_menu.png")
nimi = pygame.transform.scale(nimi, (600, nimi_y))
ekraan.blit(nimi, (700, 100))

#Lind
lind1 = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind1.png")
lind2 = pygame.image.load("E:\Mäng\M-ng\Flappy_bird2.0\Assets\Lind2.png")
lind1 = pygame.transform.scale(lind1, (300, 300))
ekraan.blit(lind1, (500, 300))

pygame.display.update()
while (mäng_töötab):

#Menüü liikumine (pooleli)
    dt = clock.tick() / 1000
    nimi_y = (100)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    nimi_y +=1

    ekraan.blit(nimi, (700, nimi_y))
    pygame.display.flip()

    pygame.time.delay(17)


pygame.display.flip()
