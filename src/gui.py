#gui for chess board

import pygame

pygame.init()
window = pygame.display.set_mode((1080, 620))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    window.fill("black")
    
    #place game here. need to draw a board, fill it in, and place pieces.
    #functionality of game should be able to be contained in functions contained elsewhere.
    


    clock.tick(60)
pygame.quit()