#!/usr/bin/env python3

import pygame
from classes.Menu import Menu
from classes.Level import Level
from classes.Const import MENU_OPTION, SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, "Level1", menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                exit()