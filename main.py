import pygame;

# Initialize pygame
pygame.init(); 
displayresolutionX,displayresolutionY=1280,720; 
# Create a screen
screen = pygame.display.set_mode((displayresolutionX,displayresolutionY)); 

#Icon and Title
pygame.display.set_caption("SPACE_DEFENDER")
icon=pygame.image.load('icon.png'); 
pygame.display.set_icon(icon); 

#Player
playerImg=pygame.image.load('spaceship.png'); 
playerX,playerY=(displayresolutionX/2)*0.95,displayresolutionY*0.9; 
playerX_change=0; 
playerY_change=0; 
speed=0.5; 

def player(X,Y):
    screen.blit(playerImg,(X,Y)); 

#Game Loop
running=True; 
while running:
    screen.fill((20,20,20)); #dark grey screen in RGB values
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False; 

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-speed; 
            if event.key==pygame.K_RIGHT:
                playerX_change=speed; 
            
            if event.key==pygame.K_UP:
                playerY_change=-speed; 
            if event.key==pygame.K_DOWN:
                playerY_change=speed; 
            

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0; 
        if event.type==pygame.KEYUP:
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
    

    player(playerX,playerY); 
    pygame.display.update(); 


