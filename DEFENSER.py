'''
顯示圖片
'''

import pygame
import math
import os
from ATTACKER import Attacker 

class Defenser:
    def __init__(self,x,y,price,rate,damage,Range,tower_imgs):
        self.imgs = tower_imgs
        self.x = x + self.imgs[0].get_width()/2
        self.y = y + self.imgs[0].get_height()/2
        self.price = price
        self.rate_of_fire = rate
        self.damage = damage
        self.range = Range
        self.width = 80
        self.height = 80
        self.tick_count = 0
        self.place_color = (0,0,255,100)    #綠色，透明度100
        self.attack_mode = 0  #沒攻擊時0，攻擊時1

    def draw(self,win):   #顯示defenser圖片
        img = self.imgs[self.attack_mode]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def attack(self, attackers):
        target_dis = 10000000
        if self.tick_count % (180//self.rate_of_fire) == 0:
            self.tick_count += 1
            for attacker in attackers:    #攻擊目標判定
                x = attacker.x
                y = attacker.y
                dis = math.sqrt((self.x - attacker.imgs[0].get_width()//2 - x)**2 + (self.y - attacker.imgs[0].get_height()//2 - y)**2)
                if dis < self.range: 
                    if dis < target_dis:
                        target = attacker
                        target_dis = dis
            if target_dis < 10000000:
                self.attack_mode = 1 
                if self.damage == 25:
                    Attacker.hit(target,self.damage,attackers)
                    self.explode(target,attackers)
                else:
                    Attacker.hit(target,self.damage,attackers)
            else:
                self.tick_count = 0  #沒有攻擊目標則重置tick 
                self.attack_mode = 0
        else:
            self.tick_count += 1
            self.attack_mode = 0

    def explode(self,target,attackers):  #大王椰範圍傷害
        x1 = target.x + target.imgs[0].get_width()//2
        y1 = target.y + target.imgs[0].get_height()//2
        for attacker in attackers:
            if target != attacker:
                x2 = attacker.x + attacker.imgs[0].get_width()//2
                y2 = attacker.y + attacker.imgs[0].get_height()//2
                dis = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if dis < 130:
                    Attacker.hit(attacker,25,attackers)

    def move(self, pos):
        """
        Move the defenser
        """
        self.x = pos[0]
        self.y = pos[1]
    
    def collide(self, other):
        """
        Check if two defensers are collided
        """
        other_x = other.x
        other_y = other.y
        if self.x - self.width < other_x < self.x + self.width:
            if self.y - self.height < other_y < self.y + self.height:
                return True
        
        return False
    
    def draw_placement(self, win):
        surface = pygame.Surface((self.width * 4, self.height * 4), pygame.SRCALPHA, 32)
        pygame.draw.rect(surface, self.place_color,[40, 40, self.width, self.height], 0)

        win.blit(surface, (self.x - 60, self.y - 60))
        
            
class Sugar(Defenser):      #砂糖椰
    def __init__(self,x,y):
        self.sugar = pygame.image.load(os.path.join('DefensersImage_matted', 'sugar.png')).convert_alpha()
        self.sugar = pygame.transform.scale(self.sugar, (80,80))
        self.sugar_1 = pygame.image.load(os.path.join('DefensersImage_matted', 'sugar-1.png')).convert_alpha()
        self.sugar_1 = pygame.transform.scale(self.sugar_1, (80,80))
        super().__init__(x,y,25,10,4,120,[self.sugar,self.sugar_1])

class Winebottle(Defenser):  #酒瓶椰
    def __init__(self,x,y):
        self.winebottle = pygame.image.load(os.path.join('DefensersImage_matted', 'winebottle.png')).convert_alpha()
        self.winebottle = pygame.transform.scale(self.winebottle, (80,80))
        self.winebottle_1 = pygame.image.load(os.path.join('DefensersImage_matted', 'winebottle-1.png')).convert_alpha()
        self.winebottle_1 = pygame.transform.scale(self.winebottle_1, (80,80))
        super().__init__(x,y,30,30,2,100,[self.winebottle,self.winebottle_1])

class Golden(Defenser):   #黃金椰
    def __init__(self,x,y):
        self.golden = pygame.image.load(os.path.join('DefensersImage_matted', 'golden.png')).convert_alpha()
        self.golden = pygame.transform.scale(self.golden, (80,80))
        self.golden_1 = pygame.image.load(os.path.join('DefensersImage_matted', 'golden-1.png')).convert_alpha()
        self.golden_1 = pygame.transform.scale(self.golden_1, (80,80))
        super().__init__(x,y,80,15,10,180,[self.golden,self.golden_1])

class King(Defenser):     #大王椰
    def __init__(self,x,y):
        self.king = pygame.image.load(os.path.join('DefensersImage_matted', 'king.png')).convert_alpha()
        self.king = pygame.transform.scale(self.king, (80,80))
        self.king_1 = pygame.image.load(os.path.join('DefensersImage_matted', 'king-1.png')).convert_alpha()
        self.king_1 = pygame.transform.scale(self.king_1, (80,80))
        super().__init__(x,y,120,5,25,80,[self.king,self.king_1])

class Ice(Defenser):     #杜老椰
    def __init__(self,x,y):
        self.ice = pygame.image.load(os.path.join('DefensersImage_matted', 'icecream.png')).convert_alpha()
        self.ice = pygame.transform.scale(self.ice, (80,80))
        self.ice_1 = pygame.image.load(os.path.join('DefensersImage_matted', 'icecream-1.png')).convert_alpha()
        self.ice_1 = pygame.transform.scale(self.ice_1, (80,80))
        super().__init__(x,y,60,20,1,210,[self.ice,self.ice_1])


    
