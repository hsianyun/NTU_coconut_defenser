'''
圖片
價格(init設定常數)
移動路徑
初始血量(init設定常數)
移動速度
對終點傷害(init設定常數)
被攻擊傷害
特殊能力
'''

import pygame
import os


class Attacker:
    def __init__(self):
        self.damage = 0
        self.width = 0 ##待改
        self.height = 0 ##待改
        self.path = [(0,500),(220,500),(220,100),(420,100),(420,260),(740,260),(740,100),(1020,100),(1020,380),(420,380),(420,500),(1200,500)]
        self.path_count = 0
        self.direction = ["R","U","R","D","R","U","R","D","L","D","R"]
        self.direction_count = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]


    # 畫圖
    def draw(self,win):
        self.img = 0 ##待改
        win.blit(self.img,(self.x - self.img.get_width()/2, self.y- self.img.get_height()/2))
    
    # 移動
    def move(self):
        if self.direction[self.direction_count] == "R":
            self.x += self.speed
        elif self.direction[self.direction_count] == "U":
            self.y += self.speed
        elif self.direction[self.direction_count] == "L":
            self.x -= self.speed
        elif self.direction[self.direction_count] == "D":
            self.y -= self.speed
        
        if self.x == self.path[self.path_count + 1][0] and self.y == self.path[self.path_count + 1][1]:
            self.path_count += 1
            self.direction_count += 1
        
         

    # 受到攻擊扣血的機制並偵測是否死亡
    def hit(self,damage,attackers):
        self.damage += damage
        if self.damage >= self.ini_blood:
            attackers.remove(self) # attackers是一個包括所有活著的attacker的list # 死亡
        if damage == 1: #杜老椰攻擊力1
            pass       #停30clk



    # 救護車補血的機制


class Pedestrian(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 2
        self.ini_blood = 10
        self.power = 1
        self.speed = 1


class Bicycle(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 10
        self.ini_blood = 30
        self.power = 2
        self.speed = 2

class Skateboard(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 4
        self.ini_blood = 10
        self.power = 1
        self.speed = 4

class Car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 50
        self.ini_blood = 100
        self.power = 5
        self.speed = 2

class Shui_yuan_car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 90
        self.ini_blood = 100
        self.power = 8
        self.speed = 1

class Ambulance(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 80
        self.ini_blood = 100
        self.power = 8
        self.speed = 2

class Student_Association(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 6
        self.ini_blood = 20
        self.power = 1
        self.speed = 2




