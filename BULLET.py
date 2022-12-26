'''
初始數值設定:   未完成:
傷害            座標(移動)
傷害範圍        圖片
飛行速度        造成傷害機制(待討論)

特殊機制:
大王椰:範圍爆炸
杜老爺:冰凍緩速
'''
class Bullet():
    def __init__(self, damage=0, range=0, speed=0):
        self.damage = damage
        self.range = range
        self.speed = speed

class HSBul(Bullet):            #香水椰子彈 HsiangShui
    def __init__(self):
        super().__init__()
        self.damage = 10
        self.range = 1
        self.speed = 10
class JPBul(Bullet):            #酒瓶椰子彈 JiuPing
    def __init__(self):
        super().__init__()
        self.damage = 5
        self.range = 1
        self.speed = 10
class GoldenBul(Bullet):            #黃金椰子彈 Golden
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.range = 2
        self.speed = 10
class KingBul(Bullet):          #大王椰子彈 King
    def __init__(self):
        super().__init__()
        self.damage = 40
        self.range = 10
        self.speed = 10
    def explode(self,Attacker):
        pass
class IceBul(Bullet):            #杜老爺子彈 Icecream
    def __init__(self,freezing):
        super().__init__()
        self.damage = 1
        self.range = 1
        self.speed = 10
        self.freezing = freezing
    def freeze(self,Attacker):
        Attacker.speed -= self.freezing



