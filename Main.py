import pygame
from pygame import key
from pygame.display import update
pygame.init()
screen = pygame.display.set_mode((660,660))
done = False
font = pygame.font.SysFont('totm.ttf', 50)
pygame.display.set_caption("Tomb color")
map = pygame.image.load('map.png')
nhanvat = pygame.image.load('nhanvat.png')
diemmap2=0
clock = pygame.time.Clock()
map_x=70
map_y=70
nhanvat_x=100
nhanvat_y=300
nhanvat_x2=130
nhanvat_y2=440
nhanvat_x3=135
nhanvat_y3=465
move_value=50
nhacnen=pygame.mixer.Sound('nhacnen.wav')
soundmove=pygame.mixer.Sound('tick.wav')
soundwin=pygame.mixer.Sound('te.wav')
white=(50,150,50)
Purple=(255,255,255)
Color=(193,50,100)
Green=(47,219,65)
Level=""
checkwin=0
while not done:
    pygame.mixer.Sound.play(nhacnen)
    x,y = pygame.mouse.get_pos()
    clock.tick(60)
    screen.fill(white)
    if checkwin==0: #chon nhan vat
        chonnhanvat = pygame.image.load('chonnv.png')
        chonnhanvat_rect = screen.blit(chonnhanvat, (0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            pygame.mixer.Sound.play(soundwin)
            nhanvat = pygame.image.load('nhanvat.png')
            checkwin=1
        if keys[pygame.K_2]:
            pygame.mixer.Sound.play(soundwin)
            nhanvat = pygame.image.load('nhanvat2.png')
            checkwin=1
        if keys[pygame.K_3]:
            pygame.mixer.Sound.play(soundwin)
            nhanvat = pygame.image.load('nhanvat3.png')
            checkwin=1
    if checkwin==1:
        text_txt = font.render("collect a key to go to next map ", True, Green)
        screen.blit(text_txt, (80, 580))
        key_x=100
        key_y=500
        khoa=pygame.image.load('key.png')
        Level=checkwin
        Level_txt = font.render("Level "+str(Level), True, Color)
        screen.blit(Level_txt, (260, 30))
        map_rect = screen.blit(map, (map_x, map_y))
        khoa_rect = screen.blit(khoa, (key_x, key_y))
        nhanvat_rect = screen.blit(nhanvat, (nhanvat_x,nhanvat_y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nhanvat_x > 100 and nhanvat_y>480:
            nhanvat_x -= move_value
            pygame.mixer.Sound.play(soundmove)
        if keys[pygame.K_RIGHT] and nhanvat_y<160 and nhanvat_x < 500:
            nhanvat_x += move_value
            pygame.mixer.Sound.play(soundmove)
        if keys[pygame.K_UP] and nhanvat_y<350 and nhanvat_y > 100:
            nhanvat_y -= move_value
            pygame.mixer.Sound.play(soundmove)
        if keys[pygame.K_DOWN]:
            pygame.mixer.Sound.play(soundmove)
            if nhanvat_x<150:
                if nhanvat_y<300:
                    nhanvat_y +=move_value
            elif nhanvat_y<500 and nhanvat_x>490:
                nhanvat_y+=move_value
        if nhanvat_x==100 and nhanvat_y==500 :
            pygame.mixer.Sound.play(soundwin)
            checkwin=2
    if checkwin==2: # map 2
        text_txt = font.render("collect a key to go to next map ", True, Green)
        screen.blit(text_txt, (80, 580))
        Level=checkwin
        checkkey=False
        key_x=190
        key_y=490
        Level_txt = font.render("Level "+str(Level), True, Color)
        screen.blit(Level_txt, (260, 30))
        map=pygame.image.load('map3.png')
        khoa=pygame.image.load('key.png')
        map_rect = screen.blit(map, (map_x, map_y))
        khoa_rect = screen.blit(khoa, (key_x, key_y))
        nhanvat2_rect = screen.blit(nhanvat, (nhanvat_x2,nhanvat_y2))
        key2 = pygame.key.get_pressed()       
        if key2[pygame.K_LEFT]:
            pygame.mixer.Sound.play(soundmove)
            if nhanvat_x2==315:
                nhanvat_x2=130
            elif nhanvat_x2==490 and nhanvat_y2==440:
                nhanvat_x2=130
            elif nhanvat_x2==490 and nhanvat_y2==160:
                nhanvat_x2=190
                if nhanvat_y2==100:
                    nhanvat_x2=130
            elif nhanvat_y2==100:
                nhanvat_x2=130
            elif nhanvat_y2==325:
                    nhanvat_x2=130
            elif nhanvat_y2==490 and nhanvat_x2==490:
                nhanvat_x2=425
            elif nhanvat_y2==320 and nhanvat_x2==490:
                nhanvat_x2=365
            elif nhanvat_x2==365 and nhanvat_y2==440:
                nhanvat_x2=130
            elif nhanvat_x2==365 and nhanvat_y2==265:
                nhanvat_x2=130
            elif nhanvat_x2==255 and nhanvat_y2==490:
                nhanvat_x2=190
            elif nhanvat_x2==320 and nhanvat_y2 ==490:
                nhanvat_x2=190
            elif nhanvat_y2==430 and nhanvat_x2==490:
                nhanvat_x2=130
                nhanvat_y2=440
            elif nhanvat_x2==320 and nhanvat_y2==380:
                nhanvat_x2=255
            elif nhanvat_x2==325 and nhanvat_y2==270:
               nhanvat_x2=130
            elif nhanvat_x2==430 and nhanvat_y2==270:
                nhanvat_x2=130
            elif nhanvat_x2==190 and nhanvat_y2==430:
                nhanvat_x2=130
        if key2[pygame.K_RIGHT]:
            pygame.mixer.Sound.play(soundmove)
            if nhanvat_y2==210:
                nhanvat_x2=315
            elif nhanvat_x2==130:
                nhanvat_x2=490
                if nhanvat_y2==325:
                    nhanvat_x2=255
                if nhanvat_y2==270:
                    nhanvat_x2=430
            elif nhanvat_x2==190:
                nhanvat_x2=490
                if nhanvat_y2==325:
                    nhanvat_x2=255
                if nhanvat_y2==490:
                    nhanvat_x2=320
            elif nhanvat_y2==100:
                nhanvat_x2=490
            elif nhanvat_y2==490 and nhanvat_x2==425:
                nhanvat_x2=490
            elif nhanvat_x2==365 and nhanvat_y2==440:
                nhanvat_x2=490
            elif nhanvat_y2==320 and nhanvat_x2==365:
                nhanvat_x2=490
            elif nhanvat_x2==365 and nhanvat_y2==265:
                nhanvat_x2=435
            elif nhanvat_x2==255 and nhanvat_y2==490:
                nhanvat_x2=320
            elif nhanvat_x2==320 and nhanvat_y2==380:
                nhanvat_x2=490
            elif nhanvat_x2==255 and nhanvat_y2==380:
                nhanvat_x2=490
            elif nhanvat_x2==315 and nhanvat_y2 ==270:
                nhanvat_x2=430
        if key2[pygame.K_UP]:
            pygame.mixer.Sound.play(soundmove)
            if nhanvat_x2==130 :
                nhanvat_y2=210
            elif nhanvat_x2==315:
                nhanvat_y2=100
            elif nhanvat_y2==160:
                nhanvat_y2=100
            elif nhanvat_y2==325:
                nhanvat_y2=100
            elif nhanvat_y2==440:
                nhanvat_y2=320
            elif nhanvat_y2==490 and nhanvat_x2==490:
                nhanvat_y2=320
            elif nhanvat_x2==365 and nhanvat_y2==320:
                nhanvat_y2=265
            elif nhanvat_y2==490:
                nhanvat_y2=100
                if nhanvat_x2==190:
                    nhanvat_y2=430
                if nhanvat_x2==320:
                    nhanvat_y2=380
            elif nhanvat_x2==435 and nhanvat_y2==265:
                nhanvat_y2=100
            elif nhanvat_x2==255 and nhanvat_y2==380:
                nhanvat_y2=100
            elif nhanvat_x2==430 and nhanvat_y2==270:
                nhanvat_y2=100
        if key2[pygame.K_DOWN]:
            pygame.mixer.Sound.play(soundmove)
            if nhanvat_y2==210:
                nhanvat_y2=440
            elif nhanvat_x2==315:
                nhanvat_y2=270
            elif nhanvat_x2==490 and nhanvat_y2==100:
                nhanvat_y2=160
            elif nhanvat_x2==190 and nhanvat_y2==160:
                nhanvat_y2=325
            elif nhanvat_y2==100 and nhanvat_x2==190:
                nhanvat_y2=325
            elif nhanvat_y2==325 and nhanvat_x2==130:
                nhanvat_y2=440
            elif nhanvat_y2==270 and nhanvat_x2==130:
                nhanvat_y2=440
            elif nhanvat_y2==440 and nhanvat_x2==490:
                nhanvat_y2=490
            elif nhanvat_y2==320 and nhanvat_x2==490:
                nhanvat_y2=490
            elif nhanvat_y2==265 and nhanvat_x2==365:
                nhanvat_y2=440
            elif nhanvat_y2==100: #
                nhanvat_y2=490 
            elif nhanvat_y2==320 and nhanvat_x2==365:
                nhanvat_y2=440
            elif nhanvat_y2==325 and nhanvat_x2==255:
                nhanvat_y2=490
            elif nhanvat_x2==190 and nhanvat_y2==430:
                nhanvat_y2=490
            elif nhanvat_x2==320 and nhanvat_y2==380:
                nhanvat_y2=490
            elif nhanvat_x2==255 and nhanvat_y2==380:
                nhanvat_y2=490
            elif nhanvat_x2==430 and nhanvat_y2==270:
                nhanvat_y2=490
        if nhanvat_x2==190 and nhanvat_y2==490:
            pygame.mixer.Sound.play(soundwin)
            diemmap2=1
            checkwin=3
    if checkwin==3: #map 3
        Level=checkwin
        font1 = pygame.font.SysFont('san', 35)
        text_txt = font1.render("collect a key to go to next map ", True, Green)
        screen.blit(text_txt, (150, 10))
        map=pygame.image.load('map2.png')
        key_x=375
        key_y=280
        khoa=pygame.image.load('key.png')
        Level_txt = font.render("Level "+str(Level), True, Color)
        screen.blit(Level_txt, (260, 30))
        map_rect = screen.blit(map, (map_x+30, map_y-10))
        khoa_rect = screen.blit(khoa, (key_x, key_y))
        nhanvat_rect = screen.blit(nhanvat, (nhanvat_x3,nhanvat_y3))    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if nhanvat_x3==440 and nhanvat_y3==465:
                nhanvat_x3=135
            elif nhanvat_x3==440 and nhanvat_y3==340:
                nhanvat_x3=195
            elif nhanvat_x3==440 and nhanvat_y3==155:
                nhanvat_x3=195
            elif nhanvat_x3==375 and nhanvat_y3==585:
                nhanvat_x3=255
            elif nhanvat_x3==255 and nhanvat_y3==280:
                nhanvat_x3=195
            elif nhanvat_x3==440 and nhanvat_y3==100:
                nhanvat_x3=375
            elif nhanvat_x3==375 and nhanvat_y3==340:
                nhanvat_x3=195
            elif nhanvat_x3==375 and nhanvat_y3==280:
                nhanvat_x3=195
            elif nhanvat_x3==375 and nhanvat_y3==525:
                nhanvat_x3=195
            elif nhanvat_x3==375 and nhanvat_y3==465:
                nhanvat_x3=135
            elif nhanvat_x3==440 and nhanvat_y3==220:
                nhanvat_x3=315
            elif nhanvat_x3==315 and nhanvat_y3==585:
                nhanvat_x3=255
            elif nhanvat_x3==315 and nhanvat_y3==155:
                nhanvat_x3=195
        if keys[pygame.K_RIGHT] :
            if nhanvat_x3==135 and nhanvat_y3==465:
                nhanvat_x3=440
            elif nhanvat_x3==195 and nhanvat_y3==155:
                nhanvat_x3=440
            elif nhanvat_x3==195 and nhanvat_y3==340:
                nhanvat_x3=440
            elif nhanvat_x3==195 and nhanvat_y3==525:
                nhanvat_x3=375
            elif nhanvat_x3==375 and nhanvat_y3==100:
                nhanvat_x3=440
            elif nhanvat_x3==375 and nhanvat_y3==340:
                nhanvat_x3=440
            elif nhanvat_x3==255 and nhanvat_y3==585:
                nhanvat_x3=375
            elif nhanvat_x3==195 and nhanvat_y3==280:
                nhanvat_x3=375
            elif nhanvat_x3==255 and nhanvat_y3==280:
                nhanvat_x3=375
            elif nhanvat_x3==375 and nhanvat_y3==465:
                nhanvat_x3=440
            elif nhanvat_x3==315 and nhanvat_y3==220:
                nhanvat_x3=440
            elif nhanvat_x3==315 and nhanvat_y3==585:
                nhanvat_x3=375
            elif nhanvat_x3==315 and nhanvat_y3==155:
                nhanvat_x3=440
        if keys[pygame.K_UP]:
            if nhanvat_x3==440 and nhanvat_y3==465:
                nhanvat_y3=340
            elif nhanvat_x3==195 and nhanvat_y3==340:
                nhanvat_y3=155
            if nhanvat_x3==440 and nhanvat_y3==155:
                nhanvat_y3=100
            elif nhanvat_x3==375 and nhanvat_y3==525:
                nhanvat_y3=465
            elif nhanvat_x3==255 and nhanvat_y3==585:
                nhanvat_y3=280
            elif nhanvat_x3==195 and nhanvat_y3==525:
                nhanvat_y3=155
            elif nhanvat_x3==195 and nhanvat_y3==280:
                nhanvat_y3=155
            elif nhanvat_x3==375 and nhanvat_y3==280:
                nhanvat_y3=100
            elif nhanvat_x3==375 and nhanvat_y3==340:
                nhanvat_y3=100
            elif nhanvat_x3==375 and nhanvat_y3==585:
                nhanvat_y3=465
            # elif nhanvat_x3==440 and nhanvat_y3==220:
            #     nhanvat_y3=100
            elif nhanvat_x3==315 and nhanvat_y3==220:
                nhanvat_y3=155
            elif nhanvat_x3==315 and nhanvat_y3==585:
                nhanvat_y3=155
        if keys[pygame.K_DOWN]:  
            if nhanvat_x3==440 and nhanvat_y3==340:
                nhanvat_y3=465
            elif nhanvat_x3==195 and nhanvat_y3==155:
                nhanvat_y3=525
            elif nhanvat_x3==375 and nhanvat_y3==525:
                nhanvat_y3=585
            elif nhanvat_x3==195 and nhanvat_y3==340:
                nhanvat_y3=525
            elif nhanvat_x3==255 and nhanvat_y3==280:
                nhanvat_y3=585
            elif nhanvat_x3==440 and nhanvat_y3==100:
                nhanvat_y3=220
            elif nhanvat_x3==440 and nhanvat_y3==155:
                nhanvat_y3=220
            elif nhanvat_x3==375 and nhanvat_y3==100:
                nhanvat_y3=340
            elif nhanvat_x3==195 and nhanvat_y3==280:
                nhanvat_y3=525
            elif nhanvat_x3==375 and nhanvat_y3==280:
                nhanvat_y3=340
            elif nhanvat_x3==375 and nhanvat_y3==100:
                nhanvat_y3=340
            elif nhanvat_x3==375 and nhanvat_y3==465:
                nhanvat_y3=585
            elif nhanvat_x3==315 and nhanvat_y3==220:
                nhanvat_y3=585
            elif nhanvat_x3==315 and nhanvat_y3==155:
                nhanvat_y3=585
        if nhanvat_x3==375 and nhanvat_y3==280:
            checkwin=4
    if checkwin==4:
        Level=checkwin
        font1 = pygame.font.SysFont('san', 35)
        text_txt = font1.render("collect a key to go to next map ", True, Green)
        screen.blit(text_txt, (150, 10))
        map=pygame.image.load('map.png')
        key_x=375
        key_y=280
        khoa=pygame.image.load('key.png')
        Level_txt = font.render("Level "+str(Level), True, Color)
        screen.blit(Level_txt, (260, 30))
        map_rect = screen.blit(map, (map_x+30, map_y-10))
        khoa_rect = screen.blit(khoa, (key_x, key_y))
        nhanvat_rect = screen.blit(nhanvat, (nhanvat_x3,nhanvat_y3))    
    for event in pygame.event.get():  # cac su kien trong game
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: #lay toa do anh
            print(x,y)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()