import pygame, sys, random  #impordin vajalikud moodulid

pygame.init()   #panen pygame käima

# ekraani seaded
screenX = 640                         #ekraani laius px
screenY = 480                         #ekraani kõrgus px
screen =  pygame.display.set_mode([screenX, screenY])  #võiks ka lõhemalt kirjutada pygame.display.set_mode(640, 480) aga siis peaks ka igal pool all panema screenX ja screenY asemele reaalsed numbrid.
pygame.display.set_caption("Ülesanne 4")     #panen mängus ekraanile pealkirja

clock = pygame.time.Clock()

p = pygame.image.load("punanef1.png")
screen.blit(p, [300, 390])  #blit-iga kuvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil


# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(2):  #sellega määran ära,et 2 autot toimetab
    posX = random.randint(150, 440)  #panen kordinaadid, mille piires X teljel võib auto ilmuda (asuda, sest auto ilmub iga framega uuesti) (NB! X telg on oluline paika panna, et autod murule ei läheks!)
    posY = random.randint(-100, 1)  #panen kordinaadid, mille piires Y teljel võib auto ilmuda (antud juhul 100px ennem kuni 1px pärast ekraani ülemist äärt ehk Y telje nullpunkti)
    speed = random.randint(1, 3) #kui neid muuta, siis saab autod pannna erineva kiirusega liikuma (arvud määravad autode kiiruste vahemiku (vahemiku kust arvuti võtab audoele kiirused), kui arvud on samad, siis mõlemal autol sama kiirus).
    coords.append([posX, posY, speed])


gameover = False
while not gameover:
    # fps
    clock.tick(60) #ära katsetamise ajal üle 60fps pane, Macil pole aktiivjahutust, läheb liiga kummaks, kui mäng pidevalt taustal suure fps-ga ketrab!!

    pygame.display.flip()  #panen pygames ekraani flippima ehk värskendama

    youWin = pygame.image.load("taust.jpg") #laadin taustapildi
    youWin = pygame.transform.scale(youWin, [640, 480])   #muudan taustapildi suuruse samaks, mis mangu suuruski
    screen.blit(youWin, [0, 0])  #kuvan tausta ekraanile, sulgudes olevad numbrid näitavad pildi ülemise vasaku nurga asukohta ekraanil

    # panen tee liikuma!
    coords2 = []   #alljärgnevalt annan muutjuale coords2 ette x ja y telje vahemikud, kus see muutuda võib
    for t in range(2):  # sellega määran ära,et 2 autot toimetab (MIKS SIIN KA 2 PEAB OLEMA?) TUNDUB SELLEPÄRAST, et RANGE ON IGAL POOL SAM!!!! Kas saan eraldi RANGE teha liikuva tee jaoks?
        posX = random.randint(0, 0)  # panen kordinaadid, mille piires X teljel võib tee ilmuda ehk liikuda
        posY = random.randint(0, 480)  # panen kordinaadid, mille piires Y teljel võib tee ilmuda ehk liikuda, teglikult ei olegi vaja kuni 480 liiguatda, piisab kui juba 50px liigatada, jääb mulje, et tee liigub. Randomiga programm ise veel ka mudab seda tee uuesti ilmumise vahemikku.
        #teglikult peaks saama natuke lihtsama lahenduse teha liikuvatee jaoks. Vaja on ju muta ainult y-telje kordinaate ja mingit randomit ei ole ju ülesandes selle kohta nõutud, võib muutuda ka konstantselt!
        speed = random.randint(1, 1)  # kui neid muuta, siis saab autod pannna erineva kiirusega liikuma (arvud määravad autode kiiruste vahemiku (vahemiku kust arvuti võtab audoele kiirused), kui arvud on samad, siis mõlemal autol sama kiirus).
        coords2.append([posX, posY, speed])

    for t in range(len(coords)):
        liikuvtee = pygame.image.load("taust.jpg")  #laadin tee pildija panen ta võrduma liikuvatee-ga

        screen.blit(liikuvtee, [0, (coords2[t][1])])  #panen screen.blit-iga sinise auto ehk a ekraaanile ja määran auto kordinaadid, kus coords[i](0) on x telje kordinaatide vahemik ja coords[i](1) on Y-telje kordinaatide vahemik
        coords2[t][1] += coords2[t][2]   #kui üleval pool kiirusele ka vahemik anda, siis hakkab lisaks autodele ka tee kohati erineva kiirusega liikuma, paneks teele mingi teistsuguse muutuja nimetuse kui autodel on annaks ainult konstanse kiiruse?


    #punane auto ja sinised autod peavad olema peale tausta, muidu taust kleebitakse nende peale ja ei näe peale tausta midagi!
    p = pygame.image.load("punanef1.png") #mõistlik vist punane sinistest alla poole viia, siis paistab mängijale, et punane sõidab üle siniste.
    screen.blit(p,[300, 390])  # blit-iga kuvame graaafikat ekraanil ja numbrid näitavad selle graaafika asukohta ekraanil

    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    for i in range(len(coords)):
        a = pygame.image.load("sininef1.png")  #laadin sinise auto ja panen ta võrduma a-ga

        screen.blit(a, [(coords[i][0]), (coords[i][1])])  #panen screen.blit-iga sinise auto ehk a ekraaanile ja määran auto kordinaadid, kus coords[i](0) on x telje kordinaatide vahemik ja coords[i](1) on Y-telje kordinaatide vahemik
        coords[i][1] += coords[i][2]  #hakkan autode asukohtasid y teljel muutma, sest hakkan suurendama coords[i](1) muutujat. Antud võrrand tähendab sisuliselt x=x+1 ehk auto asukohale hakatakse lisama iga ekraani värskendusega, auto asukoht muutub y-teljel iga ekraani värskendusega 1 pixel suuremaks ehk alla poole.


            # kui jõuab alla, siis muudame ruudu alguspunkti (EHK SIIS KORDAMINE)
        if coords[i][1] > screenY:   #kui auto kordinaadid on suuremad kui Y telje maksimaalne suurus ekraanil ehk ekraani alumine osa px, antud juhul 480px, siis võtab süsteem auto uued kordinaadid allolevatest coords vahemikest.
            coords[i][1] = random.randint(-90, -10) # autod ilmuvad uuesti Y-telje kordinaatide vahemikust -90px kuni -10px
            coords[i][0] = random.randint(150, 440) #autod ilmuvad uuesti X-telje kordinaate vahemikus 150px kuni 450px

#kuidas saada punktide lugemine ekraanile ? print -iga või on mingi muu lahendus?
print (i)

pygame.quit()
