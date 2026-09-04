import pygame
import random
import math

#initialise the pygame
pygame.init()

#creating display
screen = pygame.display.set_mode((800,600))

background_img = pygame.image.load('alien_landscape_800x600_4k_quality.png')

#title the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('arcade-game.png')
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
   screen.blit(playerImg,(x,y))

#enemy
enemyImg = pygame.image.load('alien.png')
enemyX = 370
enemyY = 50
enemyX_change = 0.1
enemyY_change = 40
def enemy(x,y):
   screen.blit(enemyImg,(x,y))

#ready - you can seen the bullet on the screen
#fire -the bulllet is currently moving
bullet_Img = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

def bullet_fire(x,y):
   global bullet_state
   bullet_state = "fire"
   screen.blit(bullet_Img,(x+16,y-10))

def isCollied(eX,eY,bX,bY):
   distance = math.sqrt(math.pow((bX - eX),2) + math.pow((bY - eY),2))
   if distance < 27:
      return True
   else:
      return False
      
#this loop is to continiously run the window
running_window = True
while running_window:

    screen.blit(background_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running_window = False

        playerImg = pygame.image.load('arcade-game.png')
        Imgposition = screen.blit(playerImg, (playerX,playerY))   

        #if ketstroke is pressed check whether its right or left
        #KEYDOWN=pressing the key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        #KEYUP=releasing the key
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT:
               playerX_change = 0
           if event.key == pygame.K_RIGHT:
            playerX_change = 0

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
              if bullet_state == "ready":
                
               bullet_X = playerX
               bullet_fire(bullet_X,bullet_Y)

   
    player(playerX,playerY)
    playerX += playerX_change

    if playerX <= 0:
       playerX = 800
    elif playerX >= 800:
       playerX = 0   

    enemy(enemyX,enemyY)

    if enemyX <= 0:
      enemyX_change = 0.1
      enemyY += enemyY_change
    elif enemyX >= 736:
      enemyX_change = -0.1
      enemyY += enemyY_change
    
    if enemyY == 450:
       enemyY = 0
   
    enemyX += enemyX_change

    #bullet moment
    if bullet_Y <= 0:
       bullet_Y = 480
       bullet_state = "ready"
    if bullet_state is "fire":
       bullet_fire(bullet_X,bullet_Y)
       bullet_Y -= bulletY_change
    collision = isCollied(enemyX,enemyY,bullet_X,bullet_Y)
    if collision:
       bullet_Y = 480
       bullet_state = "ready"
            
    pygame.display.update()