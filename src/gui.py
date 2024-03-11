#gui for chess board

import pygame

#checks if a given integer is even or odd. returns true if odd and false if even
def isOdd(int):
    int+=2
    if int % 2 == 0:
        return False
    else:
        return True
    
def initializeBoard():
    global X, Y, Z, ROWS, COLS

    board = [[0 for i in range(COLS)] for j in range(ROWS)]
    for a in board:
        for b in board:
            board[Y][X] = Z
            Z += 1
            if X < 7:
                X+=1
            elif Y < 7:
                Y+=1
                X=0
    X = 0
    Y = 0
    return board

def drawBoard(board):
    global X, Y, WINDOW, LIGHT, DARK

    for a in range(COLS):
        for b in range(ROWS):
            if isOdd(Y) == True and isOdd(X) == True and X < 8:
                pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(X*135, Y*77.5, 77.5, 77.5), 0)
                X+=1
            elif isOdd(Y) == True and isOdd(X) == False and X < 8:
                pygame.draw.rect(WINDOW, DARK, pygame.Rect(X*135, Y*77.5, 77.5, 77.5), 0)
                X+=1
            elif isOdd(Y) == False and isOdd(X) == True and X < 8:
                pygame.draw.rect(WINDOW, DARK, pygame.Rect(X*135, Y*77.5, 77.5, 77.5), 0)  
                X+=1              
            elif isOdd(Y) == False and isOdd(X) == False and X < 8:
                pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(X*135, Y*77.5, 77.5, 77.5), 0)
                X+=1
            else:
                X=0
                Y+=1

    pygame.display.flip()
    return board

pygame.init()
WINDOW = pygame.display.set_mode((1080, 620))
CLOCK = pygame.time.Clock()
RUNNING = True
LIGHT = (230, 230, 250)
DARK = (75, 0, 230)
ROWS, COLS = (8, 8)
X = 0
Y = 0
Z = 0
boardExists = False

while RUNNING:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    WINDOW.fill("black")
    
    #place game here. need to draw a board, fill it in, and place pieces.
    #functionalitY of game should be able to be contained in functions contained elsewhere.
    if boardExists == True:
        continue
    else:
        board = initializeBoard()
        drawBoard(board)
        boardExists = True

    CLOCK.tick(60)
pygame.quit()

