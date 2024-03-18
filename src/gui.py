#gui for chess boardDraw 
import pygame

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
BROOK = pygame.image.load("chess/img/black-rook.png")
BKNIGHT = pygame.image.load("chess/img/black-knight.png")
BBISHOP = pygame.image.load("chess/img/black-bishop.png")
BKING = pygame.image.load("chess/img/black-king.png")
BQUEEN = pygame.image.load("chess/img/black-queen.png")
BPAWN = pygame.image.load("chess/img/black-pawn.png")
WROOK = pygame.image.load("chess/img/white-rook.png")
WKNIGHT = pygame.image.load("chess/img/white-knight.png")
WBISHOP = pygame.image.load("chess/img/white-bishop.png")
WKING = pygame.image.load("chess/img/white-king.png")
WQUEEN = pygame.image.load("chess/img/white-queen.png")
WPAWN = pygame.image.load("chess/img/white-pawn.png")

#checks if a given integer is even or odd. returns true if odd and false if even
def isOdd(int):
    int+=2
    if int % 2 == 0:
        return False
    else:
        return True
    
#loads up 2d array for drawing and initializing boardLogic later on
def initializeBoard():
    global Z, ROWS, COLS

    boardDraw = [[0 for i in range(COLS)] for j in range(ROWS)]
    for a in range(ROWS):
        for b in range(COLS):
            boardDraw[a][b] = Z
            Z += 1
    return boardDraw 

#draws our  boardDraw and maps eaach square to our 2d array. The 2d array is used for loading the img files and game logic
def drawBoard(boardDraw):
    global WINDOW, LIGHT, DARK

    for a in range(COLS):
        for b in range(ROWS):
            if isOdd(a) == True and isOdd(b) == True and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif isOdd(a) == True and isOdd(b) == False and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif isOdd(a) == False and isOdd(b) == True and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)                
            else:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)

    pygame.display.flip()
    return boardDraw 

#called anytime a move is made. this updates the positions as well as creates the board at the beginning.
#ngl this function is so ugly. there is definitly a better way to do this
def loadImg(boardDraw, boardLogic):
    global BROOK, BBISHOP, BKNIGHT, BQUEEN, BKING, BPAWN, WROOK, WBISHOP, WKNIGHT, WQUEEN, WKING, WPAWN

    BROOK = pygame.transform.scale(BROOK, (77.5, 77.5))
    BKNIGHT = pygame.transform.scale(BKNIGHT, (77.5,77.5))
    BBISHOP = pygame.transform.scale(BBISHOP, (77.5, 77.5))
    BQUEEN = pygame.transform.scale(BQUEEN, (77.5, 77.5))
    BKING = pygame.transform.scale(BKING, (77.5,77.5))
    WROOK = pygame.transform.scale(WROOK, (77.5, 77.5))
    WKNIGHT = pygame.transform.scale(WKNIGHT, (77.5,77.5))
    WBISHOP = pygame.transform.scale(WBISHOP, (77.5, 77.5))
    WQUEEN = pygame.transform.scale(WQUEEN, (77.5,77.5))
    WKING = pygame.transform.scale(WKING, (77.5,77.5))
    BPAWN = pygame.transform.scale(BPAWN, (77.5,77.5))
    WPAWN = pygame.transform.scale(WPAWN, (77.5,77.5))

    for a in range(ROWS):
        for b in range(COLS):
            if boardLogic[a][b] == -5:
                pygame.Surface.blit(WINDOW, BROOK, boardDraw[a][b])
            elif boardLogic[a][b] == -3:
                pygame.Surface.blit(WINDOW, BKNIGHT, boardDraw[a][b])
            elif boardLogic[a][b] == -3.1:
                pygame.Surface.blit(WINDOW, BBISHOP, boardDraw[a][b])
            elif boardLogic[a][b] == -9:
                pygame.Surface.blit(WINDOW, BQUEEN, boardDraw[a][b])
            elif boardLogic[a][b] == -99:
                pygame.Surface.blit(WINDOW, BKING, boardDraw[a][b])
            elif boardLogic[a][b] == -1:
                pygame.Surface.blit(WINDOW, BPAWN, boardDraw[a][b])
            elif boardLogic[a][b] == 5:
                pygame.Surface.blit(WINDOW, WROOK, boardDraw[a][b])
            elif boardLogic[a][b] == 3:
                pygame.Surface.blit(WINDOW, WKNIGHT, boardDraw[a][b])
            elif boardLogic[a][b] == 3.1:
                pygame.Surface.blit(WINDOW, WBISHOP, boardDraw[a][b])
            elif boardLogic[a][b] == 9:
                pygame.Surface.blit(WINDOW, WQUEEN, boardDraw[a][b])
            elif boardLogic[a][b] == 99:
                pygame.Surface.blit(WINDOW, WKING, boardDraw[a][b])
            elif boardLogic[a][b] == 1:
                pygame.Surface.blit(WINDOW, WPAWN, boardDraw[a][b])
            elif boardLogic[a][b] == 0 and isOdd(a) == True and isOdd(b) == True and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif boardLogic[a][b] == 0 and isOdd(a) == True and isOdd(b) == False and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
            elif boardLogic[a][b] == 0 and isOdd(a) == False and isOdd(b) == True and b < 8:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, DARK, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)                
            else:
                 boardDraw[a][b] = pygame.draw.rect(WINDOW, LIGHT, pygame.Rect(b*77.5, a*77.5, 77.5, 77.5), 0)
    
    pygame.display.update()