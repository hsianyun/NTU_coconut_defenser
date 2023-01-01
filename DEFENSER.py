'''
顯示圖片
'''

import pygame
import math
from ATTACKER import Attacker 

class Defenser:
    def __init__(self,x,y,price,rate,damage,Range,tower_imgs):
        self.x = x
        self.y = y
        self.price = price
        self.rate_of_fire = rate
        self.damage = damage
        self.range = Range
        self.width = 40
        self.height = 40
        self.tick_count = 0
        self.place_color = (0,0,255,100)    #綠色，透明度100
        self.imgs = tower_imgs
        self.attack_mode = 0  #沒攻擊時0，攻擊時1

    def draw(self,win):   #顯示defenser圖片
        img = self.imgs[self.attack_mode]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def attack(self, attackers):
        target_dis = 10000000
        if self.tick_count % (60//self.rate_of_fire) == 0:
            self.tick_count += 1
            for attacker in attackers:    #攻擊目標判定
                x = attacker.x
                y = attacker.y
                dis = math.sqrt((self.x - attacker.img.get_width()/2 - x)**2 + (self.y - attacker.img.get_height()/2 - y)**2)
                if dis < self.range: 
                    if dis < target_dis:
                        target = attacker
                        target_dis = dis
            if target_dis < 10000000:
                self.attack_mode = 1 
                if self.damage == 120:
                    Attacker.hit(target,self.damage,attackers)
                    self.explode(target,attackers)
                else:
                    Attacker.hit(target,self.damage,attackers)
            else:
                self.tick_count = 0  #沒有攻擊目標則重置tick 
        self.attack_mode = 0

    def explode(self,target,attackers):  #範圍傷害
        x1 = target.x + target.img.get_width()/2
        y1 = target.y + target.img.get_height()/2
        for attacker in attackers:
            if target != attacker:
                x2 = attacker.x + attacker.img.get_width()/2
                y2 = attacker.y + attacker.img.get_height()/2
                dis = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
                if dis < 20:
                    Attacker.hit(attacker,120,attackers)

    def move(self, pos):
        """
        Move the defenser
        """
        self.x = pos[0] +20
        self.y = pos[1] +20
    
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
        super().__init__(x,y,25,10,4,120,["DefensersImage/sugar.png","DefensersImage/sugar1.png"])

class Winebottle(Defenser):  #酒瓶椰
    def __init__(self,x,y):
        super().__init__(x,y,30,30,2,100,["DefensersImage/winebottle.png","DefensersImage/winebottle1.png"])

class Golden(Defenser):   #黃金椰
    def __init__(self,x,y):
        super().__init__(x,y,80,15,10,180,["DefensersImage/golden.png","DefensersImage/golden1.png"])

class King(Defenser):     #大王椰
    def __init__(self,x,y):
        super().__init__(x,y,120,5,25,80,["DefensersImage/king.png","DefensersImage/king1.png"])

class Ice(Defenser):     #杜老椰
    def __init__(self,x,y):
        super().__init__(x,y,60,20,1,210,["DefensersImage/icecream.png","DefensersImage/icecream1.png"])    

