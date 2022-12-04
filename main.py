import pygame, sys, random

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ülesanne 4")

clock = pygame.time.Clock()

#graafika laadimine
punanef1 = pygame.image.load("punanef1.png")


# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 30, 30

# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(10):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])

gameover = False
while not gameover:
    # fps
    clock.tick(120)
    # mängu sulgemine ristist
    '''events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()'''
        # Lisame pildid
    youWin = pygame.image.load("taust.jpg")
    youWin = pygame.transform.scale(youWin, [640, 480])
    screen.blit(youWin, [0, 0])


    # loendist koordinaadid
    for i in range(len(coords)):
        p = pygame.image.load("punanef1.png")
        screen.blit(p, [300, 390])  #blit-iga uvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil

        s1 = pygame.image.load("sininef1.png")
        screen.blit(s1, [180, 30])

        s2 = pygame.image.load("sininef1.png")
        screen.blit(s2, [420, 190])



        #SIIT EDASI PEAKS TULEMA ANIMATSIOONI OSA, SEE KUS õppejõul on punaste kuubikute printimien ekraanil (pygame.load.rect( ....
#VÕIMALI, ET pygame.load.ract tuleb juba peale punast autot, võimalik et peale sinist autot, võiamlik et peale kõiki siniseid autosid.
    #SAMAS KAS TEE LIIGUB? KAS PUNASED AUTOD LIIGUVAD? MIda pn parem liigutada, kas punaseid autosid ja teeda erinevate kiirsutega?
    pygame.display.flip()
    screen.fill(lBlue)

    #mängu sulgemine ristist
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

pygame.quit()