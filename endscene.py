import pygame
import os
pygame.font.init()
# pygame.init()

class Endscene:
    def __init__(self, win, winner:str):
        self.win = win
        self.bg = pygame.image.load(os.path.join("game_assets","background-PVP.png"))
        self.bg = pygame.transform.scale(self.bg, (1200,600))
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        self.player = winner
        self.title_font = pygame.font.SysFont('Comicsans', 60)
        self.hint_font = pygame.font.SysFont('Comicsans', 30)
    
    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
            
            self.draw()
    
    def draw(self):
        self.win.blit(self.bg,(0,0))
        text = self.title_font.render(f'{self.player} Wins!!', 1, (255,255,255))
        self.win.blit(text, (self.width//2 - text.get_width()//2, self.height//2 - text.get_height()//2))
        text2 = self.hint_font.render('Press SPACE to continue.', 1, (255,255,255))
        self.win.blit(text2, (self.width//2 - text2.get_width()//2, 450))
        pygame.display.update()

class PveEndscene(Endscene):
    def __init__(self, win, winner: str, img):
        super().__init__(win, winner, img)
    
    def draw(self):
        self.win.blit(self.bg,(0,0))
        text = self.title_font.render('You Lose!!', 1, (255,255,255))
        self.win.blit(text, (self.width//2 - text.get_width()//2, self.height//2 - text.get_height()//2))
        text2 = self.hint_font.render('Press SPACE to continue.', 1, (255,255,255))
        self.win.blit(text2, (self.width//2 - text2.get_width()//2, 450))
        pygame.display.update()