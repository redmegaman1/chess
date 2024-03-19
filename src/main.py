import pygame
import gui
import gameLogic

def main():
    selectFlag = False
    white2Move = False

    while gui.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gui.RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN and gui.RUNNING == True and selectFlag == False:
                x, y = pygame.mouse.get_pos()
                square = gameLogic.selectSquare(x, y)
                if gameLogic.turnSequence(boardLogic, square) == white2Move:
                    selectFlag = True
                    if white2Move == False:
                        white2Move = True
                    else:
                        white2Move = False
                else:
                    print("select the other color...")
            elif event.type == pygame.MOUSEBUTTONDOWN and gui.RUNNING == True and selectFlag == True:
                x, y = pygame.mouse.get_pos()
                place = gameLogic.selectSquare(x, y)
                if gameLogic.isValidMove(boardLogic, place, square) == True:
                    gameLogic.movePiece(square, boardLogic, place, boardDraw)
                    pygame.display.flip()
                else:
                    print("it no worky like that")
                    if white2Move == False:
                        white2Move = True
                    else:
                        white2Move = False
                
                selectFlag = False

        gui.WINDOW.fill("black")
        
        #place game here. need to draw a  boardDraw, fill it in, and place pieces.
        #functionalitY of game should be able to be contained in functions contained elsewhere.
        if gui.BOARDEXISTS == True:
            continue
        else:
            boardDraw = gui.initializeBoard()
            boardLogic = gameLogic.logicalBoard()
            gui.drawBoard(boardDraw)
            gui.loadImg(boardDraw, boardLogic)
            gui.BOARDEXISTS = True

        gui.CLOCK.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()