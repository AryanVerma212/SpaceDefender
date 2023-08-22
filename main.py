import pygame; 
import random; 
import math; 

# Initialize pygame
pygame.init(); 
displayresolutionX,displayresolutionY=1280,720; 

# Create a screen
screen = pygame.display.set_mode((displayresolutionX,displayresolutionY)); 

#Icon and Title
pygame.display.set_caption("SPACE_DEFENDER")
icon=pygame.image.load('icon.png'); 
pygame.display.set_icon(icon); 

#Background
background=pygame.image.load('bg.jpg'); 

#Enemy
num_of_enemies=4; 
enemyImg=[]; 
enemyX,enemyY=[],[]; 
enemyX_change=[]; 
enemySpeed=[]; 
enemyY_change=32; 
for enemy in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png')); 
    enemyX.append(random.randint(0,displayresolutionX-32)); 
    enemyY.append(random.randint(0,displayresolutionY*0.5)); 
    enemySpeed.append(random.randint(5,10)/10.0); 
    enemyX_change.append(enemySpeed[enemy]); 
    
#Player
playerImg=pygame.image.load('spaceship.png'); 
playerX,playerY= displayresolutionX/2-32,displayresolutionY-64; 
playerX_change=0; 
playerY_change=0; 
playerSpeed=0.7; 

#Bullet
#Ready State:
bulletImg=pygame.image.load('bullet.png'); 
bulletX,bulletY=playerX,playerY; 
bulletY_change=2; 
bulletState='ready'; 
score=0; 

def player(X,Y):
    screen.blit(playerImg,(X,Y)); 

def enemy(X,Y,i):
    screen.blit(enemyImg[i],(X,Y)); 

def fireBullet(X,Y):
    global bulletState; 
    bulletState='fire'; 
    screen.blit(bulletImg,(X+16,Y+10)); 

def isCollision(enemyX,enemyY,bulletX,bulletY):
    if bulletState!='fire':
        return False; 
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2); 
    if distance<30:
        return True; 
    return False; 

#Game Loop
running=True; 
while running:
    screen.fill((20,20,20)); #dark grey screen in RGB values
    screen.blit(background,(0,0)); 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False; 

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-playerSpeed; 
            if event.key==pygame.K_RIGHT:
                playerX_change=playerSpeed; 
            
            if event.key==pygame.K_UP:
                playerY_change=-playerSpeed; 
            if event.key==pygame.K_DOWN:
                playerY_change=playerSpeed; 
        
            if event.key==pygame.K_SPACE:
                fireBullet(playerX,playerY); 
            

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0; 
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change=0; 

    
    playerX+=playerX_change; 
    if playerX>displayresolutionX-64: #64 is the size of image
        playerX=displayresolutionX-64; 
    if playerX<0:
        playerX=0; 
    
    playerY+=playerY_change; 
    if playerY>displayresolutionY-64:
        playerY=displayresolutionY-64; 
    if playerY<0:
        playerY=0; 
    
    for i in range(num_of_enemies):
        enemyX[i]+=enemyX_change[i]; 
        if enemyX[i]>displayresolutionX-64: #64 is the size of image
            enemyX_change[i]=-enemySpeed[i];  
            enemyY[i]+=enemyY_change; 
        if enemyX[i]<0:
            enemyX_change[i]=enemySpeed[i]; 
            enemyY[i]+=enemyY_change; 
        
        #Collision

        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY); 
        if collision:
            bulletState='ready'; 
            score+=1; 
            print(score); 
            enemyX[i],enemyY[i]= random.randint(0,displayresolutionX-64),0; 
        enemy(enemyX[i],enemyY[i],i); 
    
    #Bullet Movement
    if bulletY<-32: 
        bulletState='ready'; 
    if bulletState=='ready':
        bulletX,bulletY=playerX,playerY; 
    if bulletState=='fire':
        fireBullet(bulletX,bulletY); 
        bulletY-=bulletY_change; 
    
    
    player(playerX,playerY); 
    
    pygame.display.update(); 


