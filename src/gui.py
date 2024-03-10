#gui for chess board

import pygame

#checks if a given integer is even or odd. returns true if odd and false if even
def isOdd(x):
    if (x+2) % 2 == 0:
        return False
    else:
        return True

pygame.init()
WINDOW = pygame.display.set_mode((1080, 620))
CLOCK = pygame.time.Clock()
RUNNING = True
LIGHT = (230, 230, 250)
DARK = (75, 0, 230)
ROWS, COLS = (8, 8)
BOARD = [[range(64)]  * 8] * 8

while RUNNING:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    WINDOW.fill("black")
    
    #place game here. need to draw a board, fill it in, and place pieces.
    #functionality of game should be able to be contained in functions contained elsewhere.
    for x in BOARD:
        for y in BOARD:
            if isOdd(y) == True & isOdd(x) == True:
                pygame.draw.Rect(WINDOW, LIGHT, pygame.Rect(x*135, y*77.5, 77.5, 77.5), 0)
            elif isOdd(y) == True & isOdd(x) == False:
                pygame.draw.Rect(WINDOW, DARK, pygame.Rect(x*135, y*77.5, 77.5, 77.5), 0)
            elif isOdd(y) == False & isOdd(x) == True:
                pygame.draw.Rect(WINDOW, DARK, pygame.Rect(x*135, y*77.5, 77.5, 77.5), 0)                
            else:
                pygame.draw.Rect(WINDOW, LIGHT, pygame.Rect(x*135, y*77.5, 77.5, 77.5), 0)
    pygame.display.flip()

    CLOCK.tick(60)
pygame.quit()

