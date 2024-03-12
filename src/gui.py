#gui for chess board
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
    global WINDOW

    #load black pieces to board
    bRook1 = pygame.image.load("chess/img/black-rook.png")
    bRook1 = pygame.transform.scale(bRook1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bRook1, board[0][0])
    bKnight1 = pygame.image.load("chess/img/black-knight.png")
    bKnight1 = pygame.transform.scale(bKnight1, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKnight1, board[0][1])
    bBishop1 = pygame.image.load("chess/img/black-bishop.png")
    bBishop1 = pygame.transform.scale(bBishop1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bBishop1, board[0][2])
    bQueen = pygame.image.load("chess/img/black-queen.png")
    bQueen = pygame.transform.scale(bQueen, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bQueen, board[0][3])
    bKing = pygame.image.load("chess/img/black-king.png")
    bKing = pygame.transform.scale(bKing, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKing, board[0][4])
    bBishop2 = pygame.image.load("chess/img/black-bishop.png")
    bBishop2 = pygame.transform.scale(bBishop2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bBishop2, board[0][5])
    bKnight2 = pygame.image.load("chess/img/black-knight.png")
    bKnight2 = pygame.transform.scale(bKnight2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, bKnight2, board[0][6])
    bRook2 = pygame.image.load("chess/img/black-rook.png")
    bRook2 = pygame.transform.scale(bRook2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, bRook2, board[0][7])

    #load white pieces to board
    wRook1 = pygame.image.load("chess/img/white-rook.png")
    wRook1 = pygame.transform.scale(wRook1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wRook1, board[7][0])
    wKnight1 = pygame.image.load("chess/img/white-knight.png")
    wKnight1 = pygame.transform.scale(wKnight1, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKnight1, board[7][1])
    wBishop1 = pygame.image.load("chess/img/white-bishop.png")
    wBishop1 = pygame.transform.scale(wBishop1, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wBishop1, board[7][2])
    wQueen = pygame.image.load("chess/img/white-queen.png")
    wQueen = pygame.transform.scale(wQueen, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wQueen, board[7][3])
    wKing = pygame.image.load("chess/img/white-king.png")
    wKing = pygame.transform.scale(wKing, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKing, board[7][4])
    wBishop2 = pygame.image.load("chess/img/white-bishop.png")
    wBishop2 = pygame.transform.scale(wBishop2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wBishop2, board[7][5])
    wKnight2 = pygame.image.load("chess/img/white-knight.png")
    wKnight2 = pygame.transform.scale(wKnight2, (77.5,77.5))
    pygame.Surface.blit(WINDOW, wKnight2, board[7][6])
    wRook2 = pygame.image.load("chess/img/white-rook.png")
    wRook2 = pygame.transform.scale(wRook2, (77.5, 77.5))
    pygame.Surface.blit(WINDOW, wRook2, board[7][7])

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
            pygame.Surface.blit(WINDOW, wPawn, board[6][wPawnCount])
            wPawnCount += 1
            pawnCount += 1
        elif bPawnCount != bPawnArr.__len__():
            pygame.Surface.blit(WINDOW, bPawn, board[1][bPawnCount])
            bPawnCount += 1
            pawnCount += 1

    
    pygame.display.update()


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN and RUNNING == True:
            x, y = pygame.mouse.get_pos()
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
