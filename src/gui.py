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
BROOK1 = -5
BROOK2 = -5
BKNIGHT1 = -3
BKNIGHT2 = -3
BBISHOP1 = -3
BBISHOP2 = -3
BKING = -99
BQUEEN = -9
BPAWN = -1
WROOK1 = 5
WROOK2 = 5
WKNIGHT1 = 3
WKNIGHT2 = 3
WBISHOP1 = 3
WBISHOP2 = 3
WKING = 99
WQUEEN = 9
WPAWN = 1
EMPTY = 0

#checks if a given integer is even or odd. returns true if odd and false if even
def isOdd(int):
    int+=2
    if int % 2 == 0:
        return False
    else:
        return True
    
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

def loadImg(boardDraw):
    global WINDOW

    #load black pieces to boardDraw 
    bRook1 = pygame.image.load("chess/img/black-rook.png")
    bRook1 = pygame.transform.scale(bRook1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bRook1,  boardDraw[0][0])
    bKnight1 = pygame.image.load("chess/img/black-knight.png")
    bKnight1 = pygame.transform.scale(bKnight1, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKnight1,  boardDraw[0][1])
    bBishop1 = pygame.image.load("chess/img/black-bishop.png")
    bBishop1 = pygame.transform.scale(bBishop1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bBishop1,  boardDraw[0][2])
    bQueen = pygame.image.load("chess/img/black-queen.png")
    bQueen = pygame.transform.scale(bQueen, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bQueen,  boardDraw[0][3])
    bKing = pygame.image.load("chess/img/black-king.png")
    bKing = pygame.transform.scale(bKing, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKing,  boardDraw[0][4])
    bBishop2 = pygame.image.load("chess/img/black-bishop.png")
    bBishop2 = pygame.transform.scale(bBishop2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bBishop2,  boardDraw[0][5])
    bKnight2 = pygame.image.load("chess/img/black-knight.png")
    bKnight2 = pygame.transform.scale(bKnight2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKnight2,  boardDraw[0][6])
    bRook2 = pygame.image.load("chess/img/black-rook.png")
    bRook2 = pygame.transform.scale(bRook2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bRook2,  boardDraw[0][7])

    #load white pieces to boardDraw 
    wRook1 = pygame.image.load("chess/img/white-rook.png")
    wRook1 = pygame.transform.scale(wRook1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wRook1,  boardDraw[7][0])
    wKnight1 = pygame.image.load("chess/img/white-knight.png")
    wKnight1 = pygame.transform.scale(wKnight1, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKnight1,  boardDraw[7][1])
    wBishop1 = pygame.image.load("chess/img/white-bishop.png")
    wBishop1 = pygame.transform.scale(wBishop1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wBishop1,  boardDraw[7][2])
    wQueen = pygame.image.load("chess/img/white-queen.png")
    wQueen = pygame.transform.scale(wQueen, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wQueen,  boardDraw[7][3])
    wKing = pygame.image.load("chess/img/white-king.png")
    wKing = pygame.transform.scale(wKing, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKing,  boardDraw[7][4])
    wBishop2 = pygame.image.load("chess/img/white-bishop.png")
    wBishop2 = pygame.transform.scale(wBishop2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wBishop2,  boardDraw[7][5])
    wKnight2 = pygame.image.load("chess/img/white-knight.png")
    wKnight2 = pygame.transform.scale(wKnight2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKnight2,  boardDraw[7][6])
    wRook2 = pygame.image.load("chess/img/white-rook.png")
    wRook2 = pygame.transform.scale(wRook2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wRook2,  boardDraw[7][7])

    #create white and black pawn arrays for storing png
    wPawn = pygame.image.load("chess/img/white-pawn.png")
    wPawn = pygame.transform.scale(wPawn, (77.5,77.5))
    wPawnArr = [wPawn] * 8

    bPawn = pygame.image.load("chess/img/black-pawn.png")
    bPawn = pygame.transform.scale(bPawn, (77.5,77.5))
    bPawnArr = [bPawn] * 8

    #load pawns into game
    wPawnCount, bPawnCount, pawnCount = (0, 0, 0)
    
    while pawnCount < 16:
        if wPawnCount != wPawnArr.__len__():
            pygame.Surface.blit(WINDOW, wPawn, boardDraw[6][wPawnCount])
            wPawnCount += 1
            pawnCount += 1
        elif bPawnCount != bPawnArr.__len__():
            pygame.Surface.blit(WINDOW, bPawn, boardDraw[1][bPawnCount])
            bPawnCount += 1
            pawnCount += 1
    
    pygame.display.update()

def logicalBoard(boardDraw):
    global BROOK1, BROOK2, BBISHOP1, BBISHOP2, BKNIGHT1, BKNIGHT2, BQUEEN, BKING, BPAWN, WROOK1, WROOK2, WBISHOP1, WBISHOP2, WKNIGHT1, WKNIGHT2, WQUEEN, WKING, WPAWN, EMPTY, ROWS

    boardLogic = boardDraw

    boardLogic[0][0] = BROOK1
    boardLogic[0][1] = BKNIGHT1
    boardLogic[0][2] = BBISHOP1
    boardLogic[0][3] = BQUEEN
    boardLogic[0][4] = BKING
    boardLogic[0][5] = BBISHOP2
    boardLogic[0][6] = BKNIGHT2
    boardLogic[0][7] = BROOK2
    for rows in range(ROWS):
        boardLogic[1][rows] = BPAWN

    i = (0, 1, 2, 3)
    j = (0, 1,2,3,4,5,6,7)
    for x in i:
        for y in j:
            boardLogic[y][x] = EMPTY

    boardLogic[7][0] = WROOK1
    boardLogic[7][1] = WKNIGHT1
    boardLogic[7][2] = WBISHOP1
    boardLogic[7][3] = WQUEEN
    boardLogic[7][4] = WKING
    boardLogic[7][5] = WBISHOP2
    boardLogic[7][6] = WKNIGHT2
    boardLogic[7][7] = WROOK2
    for rows in range(ROWS):
        boardLogic[6][rows] = WPAWN
    return boardLogic

def selectSquare(x, y):
    global ROWS, COLS
    for col in range(COLS):
        for row in range(ROWS):
            if x > row*77 and x < (row+1)*77 and y > col *77 and y < (col+1)*77:
                return (x, y)
            else:
                continue

#def movePiece(square, boardLogic):


def main():
    global RUNNING, WINDOW, BOARDEXISTS, CLOCK
    selectFlag = False

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN and RUNNING == True and selectFlag == False:
                x, y = pygame.mouse.get_pos()
                square = selectSquare(x, y)
                selectFlag = True
            elif event.type == pygame.MOUSEBUTTONDOWN and RUNNING == True and selectFlag == True:
                movePiece(square, boardLogic)
                selectFlag = False
                

        WINDOW.fill("black")
        
        #place game here. need to draw a  boardDraw, fill it in, and place pieces.
        #functionalitY of game should be able to be contained in functions contained elsewhere.
        if BOARDEXISTS == True:
            continue
        else:
            boardDraw = initializeBoard()
            boardLogic = logicalBoard(boardDraw)
            drawBoard(boardDraw)
            loadImg(boardDraw)
            BOARDEXISTS = True

        CLOCK.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()