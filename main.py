import pygame, sys, random  #impordin vajalikud moodulid

pygame.init()   #panen pygame käima

# ekraani seaded
screenX = 640                         #ekraani laius px
screenY = 480                         #ekraani kõrgus px
screen =  pygame.display.set_mode([screenX, screenY])  #võiks ka lõhemalt kirjutada pygame.display.set_mode(640, 480) aga siis peaks ka igal pool all panema screenX ja screenY asemele reaalsed numbrid.
pygame.display.set_caption("Ülesanne 4")     #panen mängus ekraanile pealkirja
liikumise_suund = 0  #omistan muutujale "liikumise_suund väärtuse 0
skoor = 0   #skoor = 0 peab olema ennem while tsüklit, sellega seame algseks skooriks 0
clock = pygame.time.Clock()  #omistan muutujale "clock" pygame kella objekti


# koordinaatide loomine ja lisamine massiivi
coords = []   # loome listi nimega "coords" (list võrdub muutujaga "coords")
for i in range(1):  #sellega määran ära,et 1 autot tuleb siit listist, range määrab ära, et 1 elementi (0 kuni 1) ja for on tsükkel
    posX = random.randint(150, 260)  #panen kordinaadid, mille piires X teljel võib auto ilmuda (asuda, sest auto ilmub iga framega uuesti) (NB! X telg on oluline paika panna, et autod murule ei läheks!)
    posY = random.randint(-100, 0)  #panen kordinaadid, mille piires Y teljel võib auto ilmuda (antud juhul 100px ennem kuni 1px pärast ekraani ülemist äärt ehk Y telje nullpunkti)
    speed = random.randint(1, 3) #kui neid muuta, siis saab autod pannna erineva kiirusega liikuma (arvud määravad autode kiiruste vahemiku (vahemiku kust arvuti võtab audoele kiirused), kui arvud on samad, siis mõlemal autol sama kiirus).
    coords.append([posX, posY, speed]) #lisa append meetodiga coords listi lõppu muutujad posX, posY ja speed.

for i in range(1):  #sellega määran ära,et 1 auto toimetab, range määrab ära, et 1 elementi (0 kuni 1) ja for on tsükkel
    f2X = random.randint(300, 440)  #panen kordinaadid, mille piires X teljel võib auto ilmuda (asuda, sest auto ilmub iga framega uuesti) (NB! X telg on oluline paika panna, et autod murule ei läheks!)
    f2Y = random.randint(-100, 0)  #panen kordinaadid, mille piires Y teljel võib auto ilmuda (antud juhul 100px ennem kuni 1px pärast ekraani ülemist äärt ehk Y telje nullpunkti)
    speed = random.randint(1, 3) #kui neid muuta, siis saab autod pannna erineva kiirusega liikuma (arvud määravad autode kiiruste vahemiku (vahemiku kust arvuti võtab audoele kiirused), kui arvud on samad, siis mõlemal autol sama kiirus).
    coords.append([f2X, f2Y, speed]) #lisa append meetodiga coords listi lõppu muutujad posX, posY ja speed.


gameover = False   #gameover võrdub False-ga
while not gameover:  #seni kaua kuni ei ole gameover toimub alljärgnev loop
    # fps
    clock.tick(60) # sulgudes olev arv määrab, mitu korda sekundis mängu kuvatakse (antud juhul 60 korda sekundis)
#kuna liikumine on kordinaatide muutus iga kuvamisega, siis suurema frame ratega ehk clock.tick paneb mängu kiiremini
# käime. Kiiremeni saab asju liigutada ka siis, kui nende kordinaate suurema numbriga inkreenteerides.

    # mängu sulgemine ristist
    sisend = pygame.event.poll()
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:  # kui sisendi tüüp on võrdne pygame quitiga
            sys.exit()  # siis mängust väljutakse

    game_font = pygame.font.Font("freesansbold.ttf", 22)    #omistan muutujale "game_font" fondi freesansbold, 22px
    text = game_font.render("SKOOR: " + str(skoor), True, [0, 0, 0])  #  str() asemel on võimalik kasutada ka f{} .
    screen.blit(text, (5,20))   #kuvan blitiga screen peale muutuja "text", asukohaks ekraanil on x=5px ja y=20px


    pygame.display.flip()  #panen pygames ekraani flippima ehk värskendama

    youWin = pygame.image.load("taust.jpg") #laadin taustapildi
    youWin = pygame.transform.scale(youWin, [640, 480])   #muudan taustapildi suuruse samaks, mis mängu suuruski
    screen.blit(youWin, [0, 0])  #kuvan tausta ekraanile, sulgudes olevad numbrid näitavad pildi ülemise vasaku nurga asukohta ekraanil

    # panen tee liikuma!
    c2 = []   #loon tühja listi nimega "c2"
    for t in range(2):  # range on 0 kuni 1 ja for paneb loopima
        teeX = random.randint(0, 0)  # panen kordinaadid, mille piires X teljel võib tee ilmuda ehk liikuda
        teeY = random.randint(0, 480)  # panen kordinaadid, mille piires Y teljel võib tee ilmuda ehk liikuda, teglikult ei olegi vaja kuni 480 liiguatda, piisab kui juba 50px liigatada, jääb mulje, et tee liigub. Randomiga programm ise veel ka mudab seda tee uuesti ilmumise vahemikku.
        #teglikult peaks saama natuke lihtsama lahenduse teha liikuvatee jaoks. Vaja on ju muuta ainult y-telje kordinaate ja mingit randomit ei ole ju ülesandes selle kohta nõutud, võib muutuda ka konstantselt!
        speed = random.randint(1, 3)  # need arvud määravad kiiruste vahemiku (vahemiku kust arvuti võtab audoele kiirused).
        c2.append([teeX, teeY, speed]) #lisan listi c2 apeendiga teeX, teeY, speed

    for t in range(len(coords)):
        liikuvtee = pygame.image.load("taust.jpg")  #laadin tee pildija panen ta võrduma liikuvatee-ga

        screen.blit(liikuvtee, [0, (c2[t][1])])  #panen screen.blit-iga liikuva tee pildi ehk muutuja "liikuvtee"
        # ekraaanile ja määran selle kordinaadid, kus c2[i](0) on x telje kordinaatide vahemik ja c2[i](1) on Y-telje kordinaatide vahemik
        c2[t][1] += c2[t][2]


    #punane auto ja sinised autod peavad olema peale tausta, muidu taust kleebitakse nende peale ja ei näe peale tausta midagi!
    p = pygame.image.load("punanef1.png") #mõistlik vist punane sinistest alla poole viia, siis paistab mängijale, et punane sõidab üle siniste.
    '''pkast = pygame.Rect(punaneX, punaneY, 45, 90)  # omastan muutujale "pall" Rect meetodi abil loodud ristküliku asukohaga posX, posy ja suurusega 20*20px,
    screen.blit(p, pkast)'''
    screen.blit(p,[300, 390])  # blit-iga kuvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil

    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit() # kogu süsteesteemi sulgemine

    for i in range(len(coords)):
        a = pygame.image.load("sininef1.png")  #laadin sinise auto ja panen ta võrduma a-ga

        screen.blit(a, [(coords[i][0]), (coords[i][1])])  #panen screen.blit-iga sinise auto ehk a ekraaanile ja määran auto kordinaadid, kus coords[i](0) on x telje kordinaatide vahemik ja coords[i](1) on Y-telje kordinaatide vahemik
        coords[i][1] += coords[i][2]  #hakkan autode asukohtasid y teljel muutma, sest hakkan suurendama coords[i](1) muutujat. Antud võrrand tähendab sisuliselt x=x+1 ehk auto asukohale hakatakse lisama iga ekraani värskendusega, auto asukoht muutub y-teljel iga ekraani värskendusega 1 pixel suuremaks ehk alla poole.
        #eelmisel real, listist võetakse teine element ja see suureneb listi kolmanda elemendi võrra (sest listi esimene arv on 0. teine 1 ja kolmas 2, jne) Viimane listiobjekt on -1.
        #sisuliselt posY = posY + speed ehk antud juhul siis suvaline number 0-480, mis hakkab suurenema 1 kuni 3 pixli võrra iga clock.tick-iga.

            # kui jõuab alla, siis muudame ruudu alguspunkti (EHK SIIS KORDAMINE)
        if coords[i][1] > screenY:   #kui auto kordinaadid on suuremad kui Y telje maksimaalne suurus ekraanil ehk ekraani alumine osa px, antud juhul 480px, siis võtab süsteem auto uued kordinaadid allolevatest coords vahemikest.
            coords[i][1] = random.randint(-90, -10) # autod ilmuvad uuesti Y-telje kordinaatide vahemikust -90px kuni -10px
            coords[i][0] = random.randint(150, 440) #autod ilmuvad uuesti X-telje kordinaate vahemikus 150px kuni 450px
            skoor += 1