import pygame
import gui
import gameLogic

def main():
    selectFlag = False

    while gui.RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gui.RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN and gui.RUNNING == True and selectFlag == False:
                x, y = pygame.mouse.get_pos()
                square = gameLogic.selectSquare(x, y)
                selectFlag = True
            elif event.type == pygame.MOUSEBUTTONDOWN and gui.RUNNING == True and selectFlag == True:
                x, y = pygame.mouse.get_pos()
                place = gameLogic.selectSquare(x, y)
                gameLogic.movePiece(square, boardLogic, place, boardDraw)
                pygame.display.flip()
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