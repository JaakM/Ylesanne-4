import pygame, sys, random  #impordin vajalikud moodulid

pygame.init()   #panen pygame käima

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
screen =  pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ülesanne 4")

clock = pygame.time.Clock()

p = pygame.image.load("punanef1.png")
screen.blit(p, [300, 390])  #blit-iga kuvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil


# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(2):  #sellega määran ära ,et 2 autot toimetab
    posX = random.randint(150, 440)  #panen kordinaadid, mille piires X teljel võib auto asuda (NB! X telg on oluline paika panna, et autod murule ei läheks!)
    posY = random.randint(1, screenY)  #panen kordinaadid, mille piires Y teljel võib auto asuda
    speed = random.randint(1,1) #kui neid muuta, siis saab autod pannne erineva kiirusega liikuma
    coords.append([posX, posY, speed])


gameover = False
while not gameover:
    # fps
    clock.tick(60) #ära katsetamise ajal üle 60fps pane, Macil pole aktiivjahutust, läheb liga kummaks, kui mäng pidevalt taustal suure fps-ga ketrab!!

    pygame.display.flip()

    youWin = pygame.image.load("taust.jpg")
    youWin = pygame.transform.scale(youWin, [640, 480])
    screen.blit(youWin, [0, 0])

#punane auto ja sinised autod peavad olema peale tausta, muidu taust kleebitakee nende peale ja ei näe peale tausta midagi!
    p = pygame.image.load("punanef1.png") #mõistlik vist punane sinistest alla poole viia, siis paistab mängijale, et punane sõidab üle siniste."
    screen.blit(p,[300, 390])  # blit-iga uvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil

    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    for i in range(len(coords)):
        a = pygame.image.load("sininef1.png")  #laadin sinise auto ja panen ta võrduma a-ga

        screen.blit(a, [(coords[i][0]), (coords[i][1])])  #panen screen.blit-iga sinise auto ekraaanile ja määran auto kordinaadid
        coords[i][1] += coords [i][2]


            # kui jõuab alla, siis muudame ruduu alguspunkti (EHK SIIS KORDAMINE)
        if coords[i][1] > screenY:   #kui auto on üleval pool ekraani kõige suuremat Y kordinaati,
            coords[i][1] = random.randint(-90, -10)
            coords[i][0] = random.randint(150, 440)


pygame.quit()
