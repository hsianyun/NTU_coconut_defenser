'''
顯示圖片
發射子彈
碰撞偵測
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
        for attacker in attackers:
            x = attacker.x
            y = attacker.y
            dis = math.sqrt((self.x - attacker.img.get_width()/2 - x)**2 + (self.y - attacker.img.get_height()/2 - y)**2)
            if dis < self.range: #是否在攻擊範圍內
                self.inRange = True
                attacker_closest.append(attacker)

        attacker_closest.sort(key=lambda x: x.path_pos)
        attacker_closest = attacker_closest[::-1]
        if len(attacker_closest) > 0:
            target = attacker_closest[0]
            #朝目標發射子彈
            #碰撞偵測
            



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

