#!/usr/bin/env python3

import pygame
from classes.Menu import Menu
from classes.Const import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))


    def run(self):

        while True:
            menu = Menu(self.screen)

            menu.run()
