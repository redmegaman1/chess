import gui

MOVECOUNTER = 1
FIRSTPAWNMOVE = [0 * 16]
#initialize the logical representation of the chess board. used to update the location of pieces.
#i am hoping that this will be primarily used for the machine learning or computer bot that i will implement later on
def logicalBoard():
    boardLogic = [[0 for i in range(gui.COLS)] for j in range(gui.ROWS)]

    boardLogic[0][0] = -5
    boardLogic[0][1] = -3
    boardLogic[0][2] = -3.1
    boardLogic[0][3] = -9
    boardLogic[0][4] = -99
    boardLogic[0][5] = -3.1
    boardLogic[0][6] = -3
    boardLogic[0][7] = -5
    for rows in range(gui.ROWS):
        boardLogic[1][rows] = -1

    i = (0,1,2,3)
    j = (0,1,2,3,4,5,6,7)
    for x in i:
        for y in j:
            boardLogic[x+2][y] = 0
#test 2
    boardLogic[7][0] = 5
    boardLogic[7][1] = 3
    boardLogic[7][2] = 3.1
    boardLogic[7][3] = 9
    boardLogic[7][4] = 99
    boardLogic[7][5] = 3.1
    boardLogic[7][6] = 3
    boardLogic[7][7] = 5
    for rows in range(gui.ROWS):
        boardLogic[6][rows] = 1
    return boardLogic

#used for returning the selected square of the user which is then called to find the piece inside of the square
def selectSquare(x, y):
    for col in range(gui.COLS):
        for row in range(gui.ROWS):
            if x > row*77 and x < (row+1)*77 and y > col *77 and y < (col+1)*77:
                return (row, col)
            else:
                continue

#updates the logical location of the piece and calls necessary functions to update the visual location of pieces
def movePiece(square, boardLogic, place, boardDraw):

    piece = boardLogic[square[1]][square[0]]
    if piece != 0:
        #TODO: add a check valid move function
        boardLogic[square[1]][square[0]] = boardLogic[place[1]][place[0]]
        boardLogic[place[1]][place[0]] = piece
        #board image to place. must remove the image from original
        gui.drawBoard(boardDraw)
        gui.loadImg(boardDraw, boardLogic)
    else:
        print("Invalid square!")

def turnSequence(boardLogic, square):
    global MOVECOUNTER

    if gui.isOdd(MOVECOUNTER) == False and boardLogic[square[1]][square[0]] < 0:
        
        return True
    elif gui.isOdd(MOVECOUNTER) == True and boardLogic[square[1]][square[0]] > 0:
        return False
    else:
        print("selected a blank square or incorrect piece")
    return -1

def isValidMove(boardLogic, place, square): #increase movecounter here
    global MOVECOUNTER

    piece = boardLogic[square[1]][square[0]]

    #TODO only let pawns push two squares on first move using the global array declared in this file
    if piece == 1:
        if (movement(piece, place,square, boardLogic) == True or capture(piece, place, square, boardLogic) == True):
            return True
        else: 
            return False
    elif piece == -1:
        if (movement(piece, place,square, boardLogic) == True or capture(piece, place, square, boardLogic) == True):
            return True
        else: 
            return False

# check to see if a movement is attempted
def movement(piece, place, square, boardLogic):
    global MOVECOUNTER
    if (((place[1] == square[1]+2 and place[0] == square[0]) or (place[1] == square[1]+1 and place[0] == square[0])) or ((place[1] == square[1]-2 and place[0] == square[0]) or (place[1] == square[1]-1 and place[0] == square[0])) and piecePresent(piece, place, boardLogic) == False):
        MOVECOUNTER = MOVECOUNTER + 1
        return True
    else:
        return False

# check to see if a capture is intended
def capture(piece, place, square, boardLogic):
    global MOVECOUNTER
    if (piece == 1 or piece == -1):
        if ((place[1] == square[1]+1 and place[0] == square[0]+1) or (place[1] == square[1]+1 and place[0] == square[0]-1)) or ((place[1] == square[1]-1 and place[0] == square[0]-1) or (place[1] == square[1]-1 and place[0] == square[0]+1)) and piecePresent(piece, place, boardLogic) == True:
            MOVECOUNTER = MOVECOUNTER + 1
            return True
        else:
            #print(f"place 0 = {place[0]} place 1 = {place[1]} square 0 = {square[0]} square 1 = {square[1]}")
            return False

# check to see if a piece is occupying the square wanting to be moved to
def piecePresent(piece, place, boardLogic):

# if piece is white, return true if intended square contains a black piece
    if (piece > 0):
        if (boardLogic[place[1]][place[0]] < 0):
            return True
        else:
            return False
# if piece is black, return true if intended square contains a white piece
    if (piece < 0):
        if (boardLogic[place[1]][place[0]] > 0):
            return True
        else:
            return False