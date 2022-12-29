'''
顯示圖片
範圍傷害
'''

import pygame
import math

class Defenser:
    def __init__(self,x,y,price,rate,damage,Range,speed):
        self.x = x
        self.y = y
        self.price = price
        self.rate_of_fire = rate
        self.damage = damage
        self.range = Range
        self.bullet_speed = speed

    def draw(self):   #顯示圖片
        pass 

    def attack(self, attackers):
        attacker_closest = []
        target_dis = 10000000
        for attacker in attackers:    #攻擊目標判定
            x = attacker.x
            y = attacker.y
            dis = math.sqrt((self.x - attacker.img.get_width()/2 - x)**2 + (self.y - attacker.img.get_height()/2 - y)**2)
            if dis < self.range: 
                if dis < target_dis:
                    target = attacker
                    target_dis = dis
        if target_dis < 10000000:
            #朝目標攻擊
            if xxxxxx:
                return target,self.damage
            



class Suger(Defenser):      #砂糖椰
    def __init__(self,x,y):
        super().__init__(x,y,25,10,4,120,1)

class Winebottle(Defenser):  #酒瓶椰
    def __init__(self):
        super().__init__(x,y,30,25,2,100,1)

class Golden(Defenser):   #黃金椰
    def __init__(self):
        super().__init__(x,y,80,15,10,180,1)

class King(Defenser):     #大王椰
    def __init__(self):
        super().__init__(x,y,120,5,25,80,1)
        
    def explode(self):     #範圍傷害
        pass

class Ice(Defenser):     #杜老椰
    def __init__(self):
        super().__init__(x,y,60,20,1,210,1)    

