from main import pvpGame, pveGame
import pygame
import os
pygame.font.init()

start_btn = pygame.image.load(os.path.join('game_assets', 'start_btn.png')).convert_alpha()
mode_PvE_btn = pygame.image.load(os.path.join('game_assets', 'PvE_btn.png')).convert_alpha()   #needed to fill in the picture
mode_PvP_btn = pygame.image.load(os.path.join('game_assets', 'PvP_btn.png')).convert_alpha()   #needed to fill in the picture

class MainMenu:
    def __init__(self, win):
        self.width = 1200
        self.height = 600
        self.bg = pygame.image.load(os.path.join('game_assets', 'mainmenu_bg.png'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.logo = pygame.image.load(os.path.join('game_assets','logo.png'))
        self.win = win
        self.mode = 'PvP'
        self.btn_start = (self.width//2-start_btn.get_width()//2, 495, start_btn.get_width(), start_btn.get_height())
        self.pve_btn_start = 575 - mode_PvE_btn.get_width()
        self.btn_PvE = (self.pve_btn_start, 405, mode_PvE_btn.get_width(), mode_PvE_btn.get_height())
        self.btn_PvP = (625, 405, mode_PvP_btn.get_width(), mode_PvP_btn.get_height())
        self.font = pygame.font.SysFont('OCR A Extended', 45)
        self.modetext = self.font.render('Mode: '+self.mode, True, (96,78,52))

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #If user quit the window, stop the program
                    run = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()    #Get the position of mouse

                    #check if hit the buttons
                    if self.btn_start[0] <= x <= self.btn_start[0] + self.btn_start[2]:
                        if self.btn_start[1] <= y <= self.btn_start[1] + self.btn_start[3]:
                            if self.mode == 'PvP':
                                game = pvpGame(self.win, self.mode)
                            elif self.mode == 'PvE':
                                game = pveGame(self.win, self.mode)
                            game.run()      #run the game
                            del game        #After leaving the game, del the game object
                            
                    
                    if self.btn_PvE[0] <= x <= self.btn_PvE[0] + self.btn_PvE[2]:
                        if self.btn_PvE[1] <= y <= self.btn_PvE[1] + self.btn_PvE[3]:
                            self.mode = 'PvE'
                            self.modetext = self.font.render('Mode: '+self.mode, True, (0,0,0))
                    
                    if self.btn_PvP[0] <= x <= self.btn_PvP[0] + self.btn_PvP[2]:
                        if self.btn_PvP[1] <= y <= self.btn_PvP[1] + self.btn_PvP[3]:
                            self.mode = 'PvP'
                            self.modetext = self.font.render('Mode: '+self.mode, True, (0,0,0))
                

            self.draw()

        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg,(0,0))
        self.win.blit(self.logo,(self.width//2 - self.logo.get_width()//2, 50))
        self.win.blit(mode_PvE_btn, (self.pve_btn_start,405))
        self.win.blit(mode_PvP_btn, (625,405))
        self.win.blit(start_btn, (self.btn_start[0], self.btn_start[1]))
        self.win.blit(self.modetext, (self.width//2 - self.modetext.get_width()//2, 335))
        pygame.display.update()
