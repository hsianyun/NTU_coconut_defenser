import pygame

if __name__ == '__main__':
    pygame.init
    pygame.display.set_caption("NTU Coconut Tower Defenser")
    win = pygame.display.set_mode((1200, 600))
    from mainmenu import MainMenu
    mainmenu = MainMenu(win)
    mainmenu.run()
    