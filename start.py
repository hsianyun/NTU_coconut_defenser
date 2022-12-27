import pygame

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1200, 600))
    from mainmenu import MainMenu
    mainmenu = MainMenu(win)
    mainmenu.run()
    