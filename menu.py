"""
Menu in game, including Play/Pause button and Shop menu
"""

import pygame
import os
pygame.font.init()


class button:
    """
    Button class for menu object
    """
    def __init__(self, img, name, pos, cost):
        self.name = name
        self.img = img
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost
    
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
    
class PlayPauseButton(button):
    def __init__(self, play_img, pause_img, pos):
        self.play_img = play_img
        self.pause_img = pause_img
        self.x = pos[0]
        self.y = pos[1]
        self.width = self.play_img.get_width()
        self.height = self.play_img.get_height()
        self.isRunning = True
    
    def draw(self, win):
        if self.isRunning:
            win.blit(self.pause_img, (self.x, self.y))
        else:
            win.blit(self.play_img, (self.x, self.y))
    
    def clicked(self):
        """
        update the running status after been clicked
        """
        self.isRunning = not self.isRunning

        

class ShopMenu:
    def __init__(self, pos, background_img):
        self.pos = pos
        self.bg = background_img
        self.buttons = []
        self.items = 0
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()

    def add_btn(self, img, name, interval, cost):
        """
        Add a button to the menu
        :para img :surface
        :para name: name
        :para interval: int
        """
        button_pos = (self.pos[0], self.pos[1] + self.items*interval)
        self.items += 1
        self.buttons.append(button(img, name, button_pos, cost))
    
    def draw(self, win):
        win.blit(self.bg, self.pos)
        for btn in self.buttons:
            btn.draw(win)
    
    def get_cost(self, name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        
        return None

    def click(self, pos):
        for btn in self.buttons:
            if btn.click(pos):
                return btn.name
        
        return None



