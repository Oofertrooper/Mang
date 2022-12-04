dt = clock.tick() / 1000
    nimi_y = (100)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    nimi_y +=1

    ekraan.blit(nimi, (700, nimi_y))
    pygame.display.flip()

    pygame.time.delay(17)