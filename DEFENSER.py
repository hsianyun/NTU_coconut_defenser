'''
顯示圖片
'''

import pygame
import math
from ATTACKER import Attacker 

class Defenser:
    def __init__(self,x,y,price,rate,damage,Range):
        self.x = x
        self.y = y
        self.price = price
        self.rate_of_fire = rate
        self.damage = damage
        self.range = Range

    def draw(self):   #顯示圖片
        pass 

    def attack(self, attackers, tick):
        target_dis = 10000000
        if tick % 60//self.rate_of_fire == 0:
            for attacker in attackers:    #攻擊目標判定
                x = attacker.x
                y = attacker.y
                dis = math.sqrt((self.x - attacker.img.get_width()/2 - x)**2 + (self.y - attacker.img.get_height()/2 - y)**2)
                if dis < self.range: 
                    if dis < target_dis:
                        target = attacker
                        target_dis = dis
            if target_dis < 10000000:
                #defenser開火動畫
                if self.damage == 120:
                    Attacker.hit(target,self.damage,attackers)
                    self.explode(target,attackers)
                else:
                    Attacker.hit(target,self.damage,attackers)

    def explode(self,attackers,target):  #範圍傷害
        x1 = target.x + target.img.get_width()/2
        y1 = target.y + target.img.get_height()/2
        for attacker in attackers:
            if target != attacker:
                x2 = attacker.x + attacker.img.get_width()/2
                y2 = attacker.y + attacker.img.get_height()/2
                dis = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
                if dis < 20:
                    Attacker.hit(attacker,120,attackers)
        
            



class Sugar(Defenser):      #砂糖椰
    def __init__(self,x,y):
        super().__init__(x,y,25,10,4,120)

class Winebottle(Defenser):  #酒瓶椰
    def __init__(self,x,y):
        super().__init__(x,y,30,30,2,100)

class Golden(Defenser):   #黃金椰
    def __init__(self,x,y):
        super().__init__(x,y,80,15,10,180)

class King(Defenser):     #大王椰
    def __init__(self,x,y):
        super().__init__(x,y,120,5,25,80)

class Ice(Defenser):     #杜老椰
    def __init__(self,x,y):
        super().__init__(x,y,60,20,1,210)    

