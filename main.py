import pygame
import os
from ATTACKER import Pedestrian, Bicycle, Shui_yuan_car, Skateboard, Car, Ambulance, Student_Association
from DEFENSER import Sugar, Winebottle, Golden, King, Ice
from menu import PlayPauseButton, ShopMenu
import time
import random
pygame.font.init()
pygame.init()

FPS = 60
path = [(0,500),(220,500),(220,100),(420,100),(420,260),(740,260),(740,100),(1020,100),(1020,380),(420,380),(420,500),(1200,500)]
#waves settings in pve mode
#幫我寫這裡
waves = []

heart_img = pygame.image.load(os.path.join('game_assets', 'heart.png')).convert_alpha()
money_img = pygame.image.load(os.path.join('game_assets', 'money.png')).convert_alpha()
shopbg_img = pygame.image.load(os.path.join('game_assets', 'shop_bg.png')).convert_alpha()
shopbg_img2 = pygame.image.load(os.path.join('game_assets', 'shop_bg_2.png')).convert_alpha()

#檔案名待補
buy_sugar = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_wine = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_golden = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_king = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_ice = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

buy_pedestrian = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_bicycle = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_skateboard = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_car = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_shuiyuan = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_ambulance = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()
buy_sa = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

play_btn = pygame.image.load(os.path.join('game_assets', 'play_btn.png')).convert_alpha()
pause_btn = pygame.image.load(os.path.join('game_assets', 'pause_btn.png')).convert_alpha()

attacker_names = ["Pedestrian", "Bicycle", "Skateboard", "Car", "Shui_yuan_car", "Ambulance", "Student_Association"]
defenser_names = ['Sugar', 'Winebottle', 'Golden', 'King', 'Ice']

resolution = (1200, 600)    #The size of the window is (1200*600)

class Game:
    def __init__(self, win, mode):
        self.win = win
        self.mode = mode
        self.width, self.height = resolution
        self.attackers = []
        self.defensers = []
        self.lifes_def = 140
        self.money_def = 25
        self.bg = pygame.image.load(os.path.join("game_assets",""))
        self.bg = pygame.transform.scale(self.bg, resolution)
        self.timer = time.time()    #get present time
        self.life_font = pygame.font.SysFont('comicsans', 65)
        self.moving_obj = None
        self.shopmenu_def = ShopMenu((1100,0), shopbg_img)
        self.shopmenu_def.add_btn(buy_sugar, 'buy_sugar', 90, 25)
        self.shopmenu_def.add_btn(buy_wine, "buy_wine", 90, 30)
        self.shopmenu_def.add_btn(buy_golden, "buy_golden", 90, 80)
        self.shopmenu_def.add_btn(buy_king, "buy_king", 90, 120)
        self.shopmenu_def.add_btn(buy_ice, "buy_ice", 90, 160)
        self.isRunning = True   #暫停時，仍可購買物品與調整位置
        self.pause_btn = PlayPauseButton(play_btn, pause_btn, (110,10))
        self.tick_count = 0
    
    def run(self):
        pass

    def draw(self):
        self.win.blit(self.bg, (0,0))
        
        if self.moving_obj:
            self.moving_obj.draw_placement(self.win)
        
        for defenser in self.defensers:
            defenser.draw(self.win)
        
        for attacker in self.attackers:
            attacker.draw(self.win)
        
        if self.moving_obj:
            self.moving_obj.draw(self.win)

        
    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        x_grid = (x // 40) * 40
        y_grid = (y // 40) * 40
        tower_dict = {"buy_sugar": Sugar(x_grid,y_grid),
                     "buy_wine": Winebottle(x_grid,y_grid),
                     "buy_golden": Golden(x_grid, y_grid), 
                     "buy_king": King(x_grid, y_grid), 
                     "buy_ice": Ice(x_grid, y_grid)}
        
        try:
            obj = tower_dict[name]
            self.moving_obj = obj
        except Exception as e:
            print(str(e) + '"NOT VALID NAME')
    
    def is_valid(self, defenser):
        return True

class pvpGame(Game):
    def __init__(self, win, mode):
        super().__init__(win, mode)
        self.shopmenu_atk = ShopMenu((0,0), shopbg_img2)
        self.shopmenu_atk.add_btn(buy_pedestrian, "buy_pedestrian", 60, 2)
        self.shopmenu_atk.add_btn(buy_bicycle, "buy_bicycle", 60, 10)
        self.shopmenu_atk.add_btn(buy_skateboard, "buy_skateboard", 60, 4)
        self.shopmenu_atk.add_btn(buy_car, "buy_car", 60, 50)
        self.shopmenu_atk.add_btn(buy_shuiyuan, "buy_shuiyuan", 60, 90)
        self.shopmenu_atk.add_btn(buy_ambulance, "buy_ambulance", 60, 80)
        self.shopmenu_atk.add_btn(buy_sa, "buy_sa", 60, 6)
        self.money_atk = 0
        self.start_time = time.time()
    
    def run(self):
        run = True  #If run == false -> game quit
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            #Add money in rate of $5 per second
            if self.tick_count % 12 == 0:
                self.money_def += 1
                self.money_atk += 1
            
            pos = pygame.mouse.get_pos()
            pos_grid = [(pos[0]//40)*40, (pos[1]//40)*40]
            
            #check for moving object and add color under it
            if self.moving_obj:
                self.moving_obj.move(pos_grid)
                collide = False

                for defenser in self.defensers:
                    if defenser.collide(self.moving_obj):
                        collide = True
                        self.moving_obj.place_color = (255,0,0,100)
                    else:
                        if not collide: #若尚未被碰撞，設定基底顏色
                            self.moving_obj.place_color = (0,0,255,100)
            
            #event log
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    #if you are moving a tower
                    if self.moving_obj:
                        allowed = True

                        for defenser in self.defensers:
                            if defenser.collide(self.moving_obj):
                                allowed = False
                        
                        if allowed and self.is_valid(self.moving_obj):
                            self.defensers.append(self.moving_obj)
                            self.moving_obj = None
                    
                    else:
                        #check if you are pressing pause button
                        if self.pause_btn.click(pos):
                            self.isRunning = not self.isRunning
                            self.pause_btn.clicked()    #Modify the image of pause button
                        
                        #check if user is buying defenser
                        shop_button = self.shopmenu_def.click()
                        if shop_button:
                            cost = self.shopmenu_def.get_cost(shop_button)
                            if self.money_def >= cost:
                                self.money_def -= cost
                                self.add_tower(shop_button)
                        
                if event.type == pygame.KEYUP:
                    self.buy_attacker(self.attackers, event.key)

            #update the status of every object
            if self.isRunning:
                to_del = []
                for atk in self.attackers:
                    atk.move()
                    if atk.x >= path[-1][0]:
                        to_del.append(atk)
                
                for d in to_del:
                    self.lifes_def -= d.damage
                    self.attackers.remove(d)
                
                for defenser in self.defensers:
                    defenser.attack(self.attackers)

                if self.lifes_def <= 0:
                    print('Attacker Win!!')   #待改(加結束畫面)
                    run = False

                if time.time() - self.start_time >= 300:
                    print('Defenser Win!!')
                    run = False    

            self.tick_count += 1
            self.draw()

    #以鍵盤控制攻擊者的放置
    def buy_attacker(self, key):
        attackers_dict = {"buy_pedestrian": Pedestrian(), "buy_bicycle": Bicycle(), "buy_skateboard": Skateboard(),
         "buy_car": Car(), "buy_shuiyuan": Shui_yuan_car(), "buy_ambulance": Ambulance(), "buy_sa": Student_Association()}
        
        if key == pygame.K_1:
            self.add_attacker("buy_pedestrian", attackers_dict)
        elif key == pygame.K_2:
            self.add_attacker("buy_bicycle", attackers_dict)
        elif key == pygame.K_3:
            self.add_attacker("buy_skateboard", attackers_dict)
        elif key == pygame.K_3:
            self.add_attacker("buy_car", attackers_dict)
        elif key == pygame.K_3:
            self.add_attacker("buy_shuiyuan", attackers_dict)
        elif key == pygame.K_3:
            self.add_attacker("buy_ambulance", attackers_dict)
        elif key == pygame.K_3:
            self.add_attacker("buy_sa", attackers_dict)
    
    def add_attacker(self, item, attackers_dict):
        cost = self.shopmenu_atk.get_cost(item)
        if self.money_atk >= cost:
            try:
                self.attackers.append(attackers_dict[item])
                self.money_atk -= cost
            except Exception as e:
                print(str(e)+ 'NO VALID NAME')

        
        


class pveGame(Game):
    def __init__(self, win, mode):
        super().__init__(win, mode)
        self.wave = 0
        self.current_wave = waves[self.wave]
        self.wave_timer = time.time()
        self.wave_timer_en = True
    
    def run(self):
        run = True  #If run == false -> game quit
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            #Add money in rate of $5 per second
            if self.tick_count % 12 == 0:
                self.money_def += 1

            #Controll the generate of attacker
            if self.isRunning :
                if time.time() - self.timer >= random.randrange(1,6)/3: #generate attacker in random time interval
                    self.timer = time.time()
                    self.gen_attacker()
            
            pos = pygame.mouse.get_pos()
            pos_grid = [(pos[0]//40)*40, (pos[1]//40)*40]
            
            #check for moving object and add color under it
            if self.moving_obj:
                self.moving_obj.move(pos_grid)
                collide = False

                for defenser in self.defensers:
                    if defenser.collide(self.moving_obj):
                        collide = True
                        self.moving_obj.place_color = (255,0,0,100)
                    else:
                        if not collide: #若尚未被碰撞，設定基底顏色
                            self.moving_obj.place_color = (0,0,255,100)
            
            #event log
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    #if you are moving a tower
                    if self.moving_obj:
                        allowed = True

                        for defenser in self.defensers:
                            if defenser.collide(self.moving_obj):
                                allowed = False
                        
                        if allowed and self.is_valid(self.moving_obj):
                            self.defensers.append(self.moving_obj)
                            self.moving_obj = None
                    
                    else:
                        #check if you are pressing pause button
                        if self.pause_btn.click(pos):
                            self.isRunning = not self.isRunning
                            self.pause_btn.clicked()    #Modify the image of pause button
                        
                        #check if user is buying defenser
                        shop_button = self.shopmenu_def.click()
                        if shop_button:
                            cost = self.shopmenu_def.get_cost(shop_button)
                            if self.money_def >= cost:
                                self.money_def -= cost
                                self.add_tower(shop_button)
            #update the status of every object
            if self.isRunning:
                to_del = []
                for atk in self.attackers:
                    atk.move()
                    if atk.x >= path[-1][0]:
                        to_del.append(atk)
                
                for d in to_del:
                    self.lifes_def -= d.damage
                    self.attackers.remove(d)
                
                for defenser in self.defensers:
                    defenser.attack(self.attackers)

                if self.lifes_def <= 0:
                    print('You Lose')   #待改(加結束畫面)
                    run = False    

            self.tick_count += 1
            self.draw()      



    def gen_attacker(self):
        """
        Automatically generate attacker in pve mode
        """
        if sum(self.current_wave) == 0:
            if len(self.attackers) == 0:
                if self.wave_timer_en:
                    self.wave_timer = time.time()
                    self.wave_timer_en = False
                
                if time.time() - self.wave_timer >= 20:
                    self.wave += 1
                    self.current_wave = waves[self.wave]
                    self.wave_timer_en = True
            
                else:
                    wave_attackers = [Pedestrian(), Bicycle(), Skateboard(), Car(), Shui_yuan_car(), Ambulance(), Student_Association()]
                    for x in range(len(self.current_wave)):
                        if self.current_wave[x] != 0:
                            self.attackers.append(wave_attackers[x])
                            self.current_wave -= 1
                            break