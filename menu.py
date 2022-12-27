import pygame
import os
pygame.font.init()

class button:
    """
    Button class for menu object
    """
    def __init__(self, menu, img, name, pos):
        self.name = name
        self.menu = menu
        self.img = img
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    def click(self,pos):
        """
        Detect whether the button is been clicked
        :param pos: tuple(x,y)
        :return: bool
        """
        if self.x <= pos[0] <= self.x + self.width:
            if self.y <= pos[1] <= self.y + self.height:
                return True
        return False

    def draw(self, win):
        """
        Draw the button
        :param win: surface
        :return :None
        """
        win.blit(self.img, (self.x, self.y))
