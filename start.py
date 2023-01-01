import pygame

"""
遊戲名稱:大道步行
"""

if __name__ == '__main__':
    pygame.init
    pygame.display.set_caption("大道步行")
    win = pygame.display.set_mode((1200, 600))
    from mainmenu import MainMenu
    mainmenu = MainMenu(win)
    mainmenu.run()
    