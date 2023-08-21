import pygame;

# Initialize pygame
pygame.init();
displayresolutionX,displayresolutionY=1280,720;
# Create a screen
screen = pygame.display.set_mode((displayresolutionX,displayresolutionY));
screen.fill((20,20,20)); #dark grey screen in RGB values
#Icon and Title
pygame.display.set_caption("SPACE_DEFENDER")
icon=pygame.image.load('icon.png');
pygame.display.set_icon(icon);

#Player
playerImg=pygame.image.load('spaceship.png');
playerX,playerY=(displayresolutionX/2)*0.95,displayresolutionY*0.9;

def player():
    screen.blit(playerImg,(playerX,playerY));

#Game Loop
running=True;
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False;
    
    player();
    pygame.display.update();


