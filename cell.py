import pygame
from globalValues import *


class Cell(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.isAlive = False
    
    def changeStatus(self):
        if self.isAlive == False:
            self.isAlive = True
            self.image.fill(WHITE)
        else: 
            self.isAlive = False
            self.image.fill(BLUE)