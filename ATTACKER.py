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
import math


class Attacker:
    def __init__(self, pos= (0, 500)):
        self.damage = 0
        self.width = 30
        self.height = 30
        self.path = [(0,500),(220,500),(220,100),(420,100),(420,260),(740,260),(740,100),(1020,100),(1020,380),(420,380),(420,500),(1200,500)]
        self.path_count = 0
        self.direction = ["R","U","R","D","R","U","R","D","L","D","R"]
        self.direction_count = 0
        self.ice_count = -1
        self.shield = 0
        self.event = 0  # 特殊事件 1是水源車 2是救護車
        self.imgs = []
        self.animation_count = 0
        self.x = pos[0]
        self.y = pos[1]


    # 畫圖
    def draw(self,win):
        self.img = self.imgs[self.animation_count]

        win.blit(self.img,(self.x - self.img.get_width()//2, self.y- self.img.get_height()//2))
        self.draw_health_bar(win)
    
    # 移動
    def move(self):

        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        
        if self.ice_count >= 30:
            self.ice_count = -1
        elif self.ice_count >= 0:
            self.ice_count += 1
        elif self.direction[self.direction_count] == "R":
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
        

    # 血量條
    def draw_health_bar(self, win):
        length = 50
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-30, self.y - 75, health_bar, 10), 0)


    # 受到攻擊扣血的機制並偵測是否死亡
    def hit(self,damage,attackers):
        # 同溫層防護罩擋一次
        if self.shield == 1:
            self.shield -= 1
        elif damage == 1: # 杜老椰攻擊力1
            self.ice_count = 0 # 停30clk
        else:
            self.damage += damage
        # 死亡判定和特殊技能
        if self.damage >= self.ini_blood and self.event == 0:
            attackers.remove(self) # attackers 是一個包括所有活著的 attacker 的 list # 死亡
        elif self.damage >= self.ini_blood and self.event == 1:
            attackers.remove(self)
            attackers.append() # 新增腳踏車
        elif self.damage >= self.ini_blood and self.event == 2:
            attackers.remove(self)
            for attacker in attackers:
                if math.sqrt((attacker.x - self.x)**2 + (attacker.y - self.y)**2) <= 70:
                    attacker.damage = 0
        



class Pedestrian(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 2
        self.ini_blood = 10
        self.power = 1
        self.speed = 1
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "pedestrian-1.png")).convert_alpha(),
        (self.width, self.height)))
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "pedestrian-2.png")).convert_alpha(),
        (self.width, self.height)))


class Bicycle(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 10
        self.ini_blood = 30
        self.power = 2
        self.speed = 2
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "bike.png")).convert_alpha(),
        (self.width, self.height)))


class Skateboard(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 4
        self.ini_blood = 10
        self.power = 1
        self.speed = 4
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "skateboard.png")).convert_alpha(),
        (self.width, self.height)))
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "skateboard-1.png")).convert_alpha(),
        (self.width, self.height)))


class Car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 50
        self.ini_blood = 100
        self.power = 5
        self.speed = 2
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "car.png")).convert_alpha(),
        (self.width, self.height)))


class Shui_yuan_car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 90
        self.ini_blood = 100
        self.power = 8
        self.speed = 1
        self.event = 1  # 特殊事件 1是水源車 2是救護車
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "shuiyuantruck.png")).convert_alpha(),
        (self.width, self.height)))


class Ambulance(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 80
        self.ini_blood = 100
        self.power = 8
        self.speed = 2
        self.event = 2  # 特殊事件 1是水源車 2是救護車
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "ambulance.png")).convert_alpha(),
        (self.width, self.height)))



class Student_Association(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 6
        self.ini_blood = 20
        self.power = 1
        self.speed = 2
        self.shield = 1
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "SA-1.png")).convert_alpha(),
        (self.width, self.height)))
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "SA-2.png")).convert_alpha(),
        (self.width, self.height)))


