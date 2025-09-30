import gui
import gameLogic

def inCheck(piece,place,square,boardLogic):

    bKingPos = [0,0]
    wKingPos = [0,0]


    for x in range(8):
        for y in range(8):
            if boardLogic[x][y] == -99:
                bKingPos[1] = y
                bKingPos[0] = x
            elif boardLogic[x][y] == 99 :
                wKingPos[1] = y
                wKingPos[0] = x
    
    if ((boardLogic[bKingPos[1]-1][bKingPos[0]-1] == 1)
        or (boardLogic[wKingPos[1]+1][wKingPos[0]-1] == -1)
        or (boardLogic[bKingPos[1]-1][bKingPos[0]+1] == 1) 
        or (boardLogic[wKingPos[1]+1][wKingPos[0]+1] == -1)):
        return True
    else:
        return False