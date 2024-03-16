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

def lOrD(x, y):
    color = pygame.Surface.get_at(x*77, y*77)
    print(color)

def logicalBoard():
    global ROWS, COLS
    boardLogic = [[0 for i in range(COLS)] for j in range(ROWS)]

    boardLogic[0][0] = -5
    boardLogic[0][1] = -3
    boardLogic[0][2] = -3.1
    boardLogic[0][3] = -9
    boardLogic[0][4] = -99
    boardLogic[0][5] = -3.1
    boardLogic[0][6] = -3
    boardLogic[0][7] = -5
    for rows in range(ROWS):
        boardLogic[1][rows] = -1

    i = (0,1,2,3)
    j = (0,1,2,3,4,5,6,7)
    for x in i:
        for y in j:
            boardLogic[x+2][y] = 0

    boardLogic[7][0] = 5
    boardLogic[7][1] = 3
    boardLogic[7][2] = 3.1
    boardLogic[7][3] = 9
    boardLogic[7][4] = 99
    boardLogic[7][5] = 3.1
    boardLogic[7][6] = 3
    boardLogic[7][7] = 5
    for rows in range(ROWS):
        boardLogic[6][rows] = 1
    return boardLogic

def selectSquare(x, y):
    global ROWS, COLS
    for col in range(COLS):
        for row in range(ROWS):
            if x > row*77 and x < (row+1)*77 and y > col *77 and y < (col+1)*77:
                return (row, col)
            else:
                continue

def movePiece(square, boardLogic, place, boardDraw):
    global COLS, ROWS

    piece = boardLogic[square[1]][square[0]]
    if piece != 0:
        #TODO: add a check valid move function
        boardLogic[square[1]][square[0]] = boardLogic[place[1]][place[0]]
        boardLogic[place[1]][place[0]] = piece
        #board image to place. must remove the image from original
        drawBoard(boardDraw)
        loadImg(boardDraw, boardLogic)
    else:
        print("Invalid square!")

        
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
                x, y = pygame.mouse.get_pos()
                place = selectSquare(x, y)
                movePiece(square, boardLogic, place, boardDraw)
                pygame.display.flip()
                selectFlag = False
                

        WINDOW.fill("black")
        
        #place game here. need to draw a  boardDraw, fill it in, and place pieces.
        #functionalitY of game should be able to be contained in functions contained elsewhere.
        if BOARDEXISTS == True:
            continue
        else:
            boardDraw = initializeBoard()
            boardLogic = logicalBoard()
            drawBoard(boardDraw)
            loadImg(boardDraw, boardLogic)
            BOARDEXISTS = True

        CLOCK.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()