import pygame as pg;

# Initialize pygame
pg.init();

# Create a screen
screen = pg.display.set_mode((1280,720));


#Game Loop
running=True;
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False;
