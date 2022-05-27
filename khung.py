import pygame
from pygame import key
from pygame.display import update
pygame.init()
screen = pygame.display.set_mode((660,660))
done = False
font = pygame.font.SysFont('san', 50)
pygame.display.set_caption("Tomb color")
map = pygame.image.load('map.jpg')
nhanvat = pygame.image.load('nhanvat.png')
clock = pygame.time.Clock()
map_x=70
map_y=70
nhanvat_x=100
nhanvat_y=300
move_value=50
white=(255,100,255)
Purple=(255,255,255)
Color=(193,50,100)
Green=(47,219,65)
Level=""
checkwin=1
while not done:
    x,y = pygame.mouse.get_pos()
    clock.tick(60)
    screen.fill(white)
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
        if keys[pygame.K_RIGHT] and nhanvat_y<160 and nhanvat_x < 500:
            nhanvat_x += move_value
        if keys[pygame.K_UP] and nhanvat_y<350 and nhanvat_y > 100:
            nhanvat_y -= move_value
        if keys[pygame.K_DOWN]:
            if nhanvat_x<150:
                if nhanvat_y<300:
                    nhanvat_y +=move_value
            elif nhanvat_y<500 and nhanvat_x>490:
                nhanvat_y+=move_value
        if nhanvat_x==100 and nhanvat_y==500 :
            checkwin=2
    for event in pygame.event.get():  # cac su kien trong game
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: #lay toa do anh
            print(x,y)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()