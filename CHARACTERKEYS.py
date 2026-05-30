import pygame 
from pygame.locals import *
from time import *

pygame.init()

Screen=pygame.display.set_mode((800,600))
player_x =200
player_y=200
keys=[False, False, False, False]
player=pygame.image.load("IMG1.png")
BackGround=pygame.image.load("BackgroundIMG.jpg")
BG=pygame.transform.scale(BackGround,(800,600))

while player_y < 600:
    Screen.blit(BG, (0,0))
    Screen.blit(player, (player_x, player_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            if event.key==K_LEFT:
                keys[1]=True
            if event.key==K_RIGHT:
                keys[2]=True
            if event.key==K_DOWN:
                keys[3]=True

        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            if event.key==K_LEFT:
                keys[1]=False
            if event.key==K_RIGHT:
                keys[2]=False
            if event.key==K_DOWN:
                keys[3]=False

    if keys[0]:
        if player_y > 0:
            player_y=player_y - 10

    if keys[3]:
        if player_y < 580:
            player_y=player_y + 5

    if keys[1]:
        if player_x > 0:
            player_x=player_x - 5
            
    if keys[2]:
        if player_x < 750:
            player_x=player_x + 5


    player_y=player_y + 5
    sleep(0.05)
print("Game Over")
