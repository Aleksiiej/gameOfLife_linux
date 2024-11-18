import pygame
import sys
from globalValues import *
from map import prepareMap

class Game:
    def __init__(self):
        pygame.init()
        self.screen_ = pygame.display.set_mode(SCREENSIZE)
        self.clock_ = pygame.time.Clock()
        self.map_ = []
        self.initNewGame()
    
    def initNewGame(self):
        self.running_ = True
        self.map_ = prepareMap()
        self.render()

    def run(self):
        while True:
            self.showMainMenuText()

            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                while True:

                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.gameLoop()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.handleMouseInput()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        pass

                    if not self.running_:
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN:
                                break
                        self.initNewGame()
                        break

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pygame.quit()
                sys.exit()
            else:
                pass

    def handleMouseInput(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        columnIndex = int(mouseX / CELL_SIZE)
        rowIndex = int(mouseY / CELL_SIZE)
        self.map_[rowIndex][columnIndex] = True if self.map_[rowIndex][columnIndex] == False else False
        self.render()

    def gameLoop(self):
        while self.running_:
            self.processInput()
            self.update()
            self.render()
            self.clock_.tick(FPS)
    
    def processInput(self):
        pass

    def update(self):
        pass

    def render(self):
        self.screen_.fill(BLACK)
        color = BLACK
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if self.map_[i][j] == False:
                    color = BLUE
                else: color = WHITE
                pygame.draw.rect(self.screen_, color, pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2))
        pygame.display.flip()

    def showMainMenuText(self):
        self.render()
        pygame.display.flip()