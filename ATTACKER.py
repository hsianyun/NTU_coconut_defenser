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

'''
test
def __str__(self):
    return f"price{self.price}\ndamage{self.damage}"

'''

class Attacker:
    def __init__(self):
        self.damage = 0

    # 受到攻擊扣血的機制並偵測是否死亡
    def getdamage(self,xxx):
        self.damage += xxx
        if self.damage >= self.ini_blood:
            print("GG")  # 死亡

    # 血量歸零時死亡的機制

    # 救護車補血的機制

    # 被下雨打到減速的機制

class Pedestrian(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 2
        self.ini_blood = 10
        self.power = 1


class Bicycle(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 10
        self.ini_blood = 30
        self.power = 2

class Skateboard(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 4
        self.ini_blood = 10
        self.power = 1

class Car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 50
        self.ini_blood = 100
        self.power = 5

class Shui_yuan_car(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 90
        self.ini_blood = 100
        self.power = 8

class Ambulance(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 80
        self.ini_blood = 100
        self.power = 8

class Student_Association(Attacker):
    def __init__(self):
        super().__init__()
        self.price = 6
        self.ini_blood = 20
        self.power = 1


