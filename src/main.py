import pygame
import gui

WINDOW = pygame.display.set_mode((1000, 620))
CLOCK = pygame.time.Clock()
RUNNING = True
BOARDEXISTS = False

def main():
    global RUNNING, WINDOW, BOARDEXISTS, CLOCK
    selectFlag = False

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN and RUNNING == True and selectFlag == False:
                x, y = pygame.mouse.get_pos()
                square = gui.selectSquare(x, y)
                selectFlag = True
            elif event.type == pygame.MOUSEBUTTONDOWN and RUNNING == True and selectFlag == True:
                x, y = pygame.mouse.get_pos()
                place = gui.selectSquare(x, y)
                gui.movePiece(square, boardLogic, place, boardDraw)
                pygame.display.flip()
                selectFlag = False
                

        WINDOW.fill("black")
        
        #place game here. need to draw a  boardDraw, fill it in, and place pieces.
        #functionalitY of game should be able to be contained in functions contained elsewhere.
        if BOARDEXISTS == True:
            continue
        else:
            boardDraw = gui.initializeBoard()
            boardLogic = gui.logicalBoard()
            gui.drawBoard(boardDraw)
            gui.loadImg(boardDraw, boardLogic)
            BOARDEXISTS = True

        CLOCK.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()