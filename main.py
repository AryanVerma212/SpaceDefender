import pygame;

# Initialize pygame
pygame.init();
displayresolutionX,displayresolutionY=1280,720;
# Create a screen
screen = pygame.display.set_mode((displayresolutionX,displayresolutionY));
screen.fill((255,0,0));
#Icon and Title
pygame.display.set_caption("SPACE_DEFENDER")
icon=pygame.image.load('icon.png');
pygame.display.set_icon(icon);

#Game Loop
running=True;
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False;
    
    pygame.display.update();


