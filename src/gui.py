#gui for chess board
import pygame
import sys

#global variables
pygame.init()
WINDOW = pygame.display.set_mode((1000, 620))
CLOCK = pygame.time.Clock()
RUNNING = True
LIGHT = (230, 230, 250)
DARK = (75, 0, 230)
ROWS, COLS = (8, 8)
Z = 0
BOARDEXISTS = False

#checks if a given integer is even or odd. returns true if odd and false if even
def isOdd(int):
    int+=2
    if int % 2 == 0:
        return False
    else:
        return True
    
def initializeBoard():
    global Z, ROWS, COLS

    board = [[0 for i in range(COLS)] for j in range(ROWS)]
    for a in range(ROWS):
        for b in range(COLS):
            board[a][b] = Z
            Z += 1
    return board

#draws our board and maps eaach square to our 2d array. The 2d array is used for loading the img files and game logic
def drawBoard(board):
    global WINDOW, LIGHT, DARK

    for a in range(COLS):
        for b in range(ROWS):
            if isOdd(a) == True and isOdd(b) == True and b < 8:
                board[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif isOdd(a) == True and isOdd(b) == False and b < 8:
                board[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif isOdd(a) == False and isOdd(b) == True and b < 8:
                board[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)                
            else:
                board[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)

    pygame.display.flip()
    return board

def loadImg(board):
    bBishop = pygame.image.load("chess/img/black-bishop.png")
    bBishop = pygame.Surface.convert(bBishop)
    pygame.Surface.blit(WINDOW, bBishop, (900,600))
    bKing = pygame.image.load("chess/img/black-king.png")
    bKing = pygame.Surface.convert(bBishop)


while RUNNING:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            RUNNING = False
    WINDOW.fill("black")
    
    #place game here. need to draw a board, fill it in, and place pieces.
    #functionalitY of game should be able to be contained in functions contained elsewhere.
    if BOARDEXISTS == True:
        continue
    else:
        board = initializeBoard()
        drawBoard(board)
        loadImg(board)
        BOARDEXISTS = True

    CLOCK.tick(60)
pygame.quit()
