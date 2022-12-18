import pygame
import time
import sys
pygame.init()
clock = pygame.time.Clock()
#Aken
pygame.display.set_caption("Flappy")
icon = pygame.image.load("Assets\Lind1.png")
pygame.display.set_icon(icon)
mäng_töötab = True
skoor = 0

#Pildid
ekraan = pygame.display.set_mode(([2000, 1000]), pygame.WINDOWMAXIMIZED)
ekraan.fill([133, 193, 233])
taust = pygame.image.load("Assets\Taust_õhtu.png")
taust = pygame.transform.smoothscale(taust, ekraan.get_size())
ekraan.blit(taust, (0, 0))
nimi_y = 300
nimi = pygame.image.load("Assets\Flappy_menu.png")
nimi = pygame.transform.scale(nimi, (600, nimi_y))
ekraan.blit(nimi, (700, 100))

#Lind
lind1 = pygame.image.load("Assets\Lind1.png")
lind2 = pygame.image.load("Assets\Lind2.png")
lind1 = pygame.transform.scale(lind1, (300, 300))
ekraan.blit(lind1, (500, 300))

#skoor
pygame.font.init
skoor = int(5)
font = pygame.font.Font(Skoor_font, 150)



pygame.display.update()
mäng_töötab = True
while mäng_töötab:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mäng_töötab = False
    #Skoor
    ekraan.blit(taust, (0, 0), (0, 0, 300, 100))
    skoor_tekst = font.render(str(skoor), True, (255, 255, 255))
    ekraan.blit(skoor_tekst, (10, 10))
    skoor += int(1)
    pygame.display.update()
    pygame.time.delay(17)
pygame.quit()
