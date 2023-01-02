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
    def __init__(self, pos= (0, 500), pc = 0, dc = 0):
        self.damage = 0
        self.width = 40
        self.height = 40
        self.path = [(0,500),(220,500),(220,100),(420,100),(420,260),(780,260),(780,100),(1060,100),(1060,380),(420,380),(420,500),(1200,500)]
        self.path_count = pc
        self.direction = ["R","U","R","D","R","U","R","D","L","D","R"]
        self.direction_count = dc
        self.ice_count = -1
        self.shield = 0
        self.event = 0  # 特殊事件 1是水源車 2是救護車
        self.ini_blood = 0
        self.imgs = []
        self.animation_count = 0
        self.x = pos[0]
        self.y = pos[1]


    # 畫圖
    def draw(self,win):
        if self.animation_count == -1:
            self.img = self.imgs[0]
        else:
            self.img = self.imgs[self.animation_count//10]
        if self.direction[self.direction_count] == "L":
            self.img = pygame.transform.rotate(self.img, 270)
        elif self.direction[self.direction_count] == "D":
            self.img = pygame.transform.rotate(self.img, 0)
        elif self.direction[self.direction_count] == "R":
            self.img = pygame.transform.rotate(self.img, 90)
        elif self.direction[self.direction_count] == "U": 
            self.img = pygame.transform.rotate(self.img, 180)
        win.blit(self.img,(self.x - self.img.get_width()//2, self.y- self.img.get_height()//2))
        self.draw_health_bar(win)
    
    # 移動
    def move(self):

        if self.animation_count >= 0:
            self.animation_count += 1
            if self.animation_count == 20:
                self.animation_count = 0
        
        if self.ice_count >= 30:
            self.ice_count = -1
        elif self.ice_count >= 0:
            self.ice_count += 1
        elif self.direction[self.direction_count] == "R":
            self.x += self.speed
        elif self.direction[self.direction_count] == "U":
            self.y -= self.speed
        elif self.direction[self.direction_count] == "L":
            self.x -= self.speed
        elif self.direction[self.direction_count] == "D":
            self.y += self.speed
        
        if self.x == self.path[self.path_count + 1][0] and self.y == self.path[self.path_count + 1][1]:
            self.path_count += 1
            self.direction_count += 1
        

    # 血量條
    def draw_health_bar(self, win):
        length = 50
        health_bar = round(length * (self.ini_blood - self.damage) // self.ini_blood)

        pygame.draw.rect(win, (255,0,0), (self.x - 25, self.y - 35, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 25, self.y - 35, health_bar, 10), 0)


    # 受到攻擊扣血的機制並偵測是否死亡
    def hit(self,damage,attackers):
        # 同溫層防護罩擋一次
        if self.shield == 1:
            self.shield -= 1
        elif damage == 1: # 杜老椰攻擊力1
            self.ice_count = 0 # 停30clk
            self.damage += damage
        else:
            self.damage += damage
        # 死亡判定和特殊技能
        if self.damage >= self.ini_blood and self.event == 0:
            attackers.remove(self) # attackers 是一個包括所有活著的 attacker 的 list # 死亡
        elif self.damage >= self.ini_blood and self.event == 1:
            
            for _ in range(3):
                x_in, y_in = Attacker.positionjudge(self.x, self.y)
                print(x_in, y_in)
                attackers.append(Bicycle((self.x // 2 * 2, self.y // 2 * 2), x_in, y_in)) # 新增腳踏車

            attackers.remove(self)

        elif self.damage >= self.ini_blood and self.event == 2:
            attackers.remove(self)
            for attacker in attackers:
                if math.sqrt((attacker.x - self.x)**2 + (attacker.y - self.y)**2) <= 70:
                    attacker.damage = 0

    @staticmethod
    def positionjudge(x,y):
        if x >= 0 and x < 220 and y == 500:
            return 0, 0
        elif x == 220 and x <= 500 and x > 100:
            return 1, 1
        elif x >= 220 and x < 420 and y == 100:
            return 2, 2
        elif x == 420 and y >= 100 and y < 260:
            return 3, 3
        elif x >= 420 and x < 780 and y == 260:
            return 4, 4
        elif x == 780 and y <= 260 and y > 100:
            return 5, 5
        elif x >= 780 and x < 1060 and y == 100:
            return 6, 6
        elif x == 1060 and y > 100 and y < 380:
            return 7, 7
        elif x <= 1060 and x > 420 and y == 380:
            return 8, 8
        elif x == 420 and y >= 380 and y < 500:
            return 9, 9
        elif x >= 420 and x < 1200 and y == 500:
            return 10, 10
    

class Pedestrian(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 2
        self.ini_blood = 10
        self.power = 1
        self.speed = 1
        self.animation_count = 0
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "pedestrian-1.png")).convert_alpha(),
        (self.width, self.height)))
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "pedestrian-2.png")).convert_alpha(),
        (self.width, self.height)))


class Bicycle(Attacker):
    def __init__(self,pos=(0,500),pc = 0, dc = 0):
        super().__init__(pos, pc, dc)
        self.price = 10
        self.ini_blood = 30
        self.power = 2
        self.speed = 2
        self.animation_count = -1
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
        self.animation_count = 0
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
        self.animation_count = -1
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
        self.animation_count = -1
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
        self.animation_count = -1
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
        self.animation_count = 0
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "SA-1.png")).convert_alpha(),
        (self.width, self.height)))
        self.imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("AttackersImage_matted", "SA-2.png")).convert_alpha(),
        (self.width, self.height)))