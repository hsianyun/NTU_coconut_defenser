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
#waves settings in pve mode
#幫我寫這裡
waves = []

heart_img = pygame.image.load(os.path.join('game_assets', 'heart.png')).convert_alpha()
money_img = pygame.image.load(os.path.join('game_assets', 'money.png')).convert_alpha()
shopbg_img = pygame.image.load(os.path.join('game_assets', 'shop_bg.png')).convert_alpha()
shopbg_img2 = pygame.image.load(os.path.join('game_assets', 'shop_bg_2.png')).convert_alpha()

#檔案名待補
buy_sugar = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_wine = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_golden = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_king = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_ice = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

buy_pedestrian = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_bicycle = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_skateboard = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_car = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_shuiyuan = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_ambulance = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_sa = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

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
        self.bg = pygame.image.load(os.path.join("game_assets",""))
        self.bg = pygame.transform.scale(self.bg, resolution)
        self.timer = time.time()
        self.life_font = pygame.font.SysFont('comicsans', 65)
        self.moving_obj = None
        self.shopmenu_def = ShopMenu((1100,0), shopbg_img)
        self.shopmenu_def.add_btn(buy_sugar, 'buy_sugar', 90)
        self.shopmenu_def.add_btn(buy_wine, "buy_wine", 90)
        self.shopmenu_def.add_btn(buy_golden, "buy_golden", 90)
        self.shopmenu_def.add_btn(buy_king, "buy_king", 90)
        self.shopmenu_def.add_btn(buy_ice, "but_ice", 90)
        self.isRunning = True   #暫停時，仍可購買物品與調整位置
        self.pause_btn = PlayPauseButton(play_btn, pause_btn, (110,10))

class pvpGame(Game):
    def __init__(self, win, mode):
        super().__init__(win, mode)
        self.shopmenu_atk = ShopMenu((0,0), shopbg_img2)
        self.shopmenu_atk.add_btn(buy_pedestrian, "buy_pedestrian", 60)
        self.shopmenu_atk.add_btn(buy_bicycle, "buy_bicycle", 60)
        self.shopmenu_atk.add_btn(buy_skateboard, "buy_skateboard", 60)
        self.shopmenu_atk.add_btn(buy_car, "buy_car", 60)
        self.shopmenu_atk.add_btn(buy_shuiyuan, "buy_shuiyuan", 60)
        self.shopmenu_atk.add_btn(buy_ambulance, "buy_ambulance", 60)
        self.shopmenu_atk.add_btn(buy_sa, "buy_sa", 60)
        self.money_atk = 0
    

#"Pedestrian", "Bicycle", "Skateboard", "Car", "Shui_yuan_car", "Ambulance", "Student_Association"

class pveGame(Game):
    def __init__(self, win, mode):
        super().__init__(win, mode)
        self.wave = 0
        self.current_wave = waves[self.wave]
        