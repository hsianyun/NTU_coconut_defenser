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
        self.width = ##
        self.height = ##
        self.path = ##
        self.x = self.path[0][0]
        self.y = self.path[0][1]


    # 畫圖
    def draw(self,win):
        self.img = ##
        win.blit(self.img,(self.x - self.img.get_width()/2, self.y- self.img.get_height()/2))
    
    # 移動路徑
    def move(self):

    # 受到攻擊扣血的機制並偵測是否死亡
    def hit(self,damage):
        self.damage += damage
        if self.damage >= self.ini_blood:
            print("GG") # 死亡
            attackers.remove(self) #attackers是一個包括所有活著的attacker的list
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


