import pygame
import os
from ATTACKER import Pedestrian, Bicycle, Shui_yuan_car, Skateboard, Car, Ambulance, Student_Association
from DEFENSER import Sugar, Winebottle, Golden, King, Ice
from menu import PlayPauseButton, ShopMenu
import time
import random
pygame.font.init()
pygame.init()

FPS = 60
path = [(-10, 224),(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 492), (740, 504), (580, 542), (148, 541), (10, 442), (-20, 335), (-75, 305), (-100, 345)]

heart_img = pygame.image.load(os.path.join('game_assets', 'heart.png')).convert_alpha()
money_img = pygame.image.load(os.path.join('game_assets', 'money.png')).convert_alpha()
shopbg_img = pygame.image.load(os.path.join('game_assets', 'shop_bg.png')).convert_alpha()

play_btn = pygame.image.load(os.path.join('game_assets', 'play_btn.png')).convert_alpha()
pause_btn = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

attacker_names = ["Pedestrian", "Bicycle", "Skateboard", "Car", "Shui_yuan_car", "Ambulance", "Student_Association"]
defenser_names = ['Sugar', 'Winebottle', 'Golden', 'King', 'Ice']

resolution = (1200, 600)    #The size of the window is (1200*600)

class Game:
    def __init__(self, win, mode):
        self.win = win
        self.mode = mode
        self.width, self.height = resolution
        self.attackers = []
        self.defensers = []
        self.lifes_def = 140
        self.money_def = 25
        self.money_atk = 0
        