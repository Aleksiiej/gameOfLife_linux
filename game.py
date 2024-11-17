import pygame
import sys
from globalValues import *
from map import prepareMap

class Game:
    def __init__(self):
        pygame.init()
        self.screen_ = pygame.display.set_mode(SCREENSIZE)
        self.clock_ = pygame.time.Clock()
        self.initNewGame()
    
    def initNewGame(self):
        self.cellGroup = pygame.sprite.Group()
        prepareMap(self.cellGroup)
        self.running_ = True
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
                        mouseX, mouseY = pygame.mouse.get_pos()
                        for cell in self.cellGroup:
                            if cell.rect.collidepoint(mouseX, mouseY):
                                cell.changeStatus()
                        self.render()
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

    def gameLoop(self):
        while self.running_:
            self.processInput()
            self.update()
            self.render()
            self.clock_.tick(FPS)
    
    def processInput(self):
        pass

    def update(self):
        self.cellGroup.update()

    def render(self):
        self.screen_.fill(BLACK)
        self.cellGroup.draw(self.screen_)
        pygame.display.flip()

    def showMainMenuText(self):
        self.render()
        pygame.display.flip()