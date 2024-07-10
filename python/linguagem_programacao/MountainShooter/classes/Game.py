#!/usr/bin/env python3

import pygame
from classes.Menu import Menu
from classes.Level import Level
from classes.Const import MENU_OPTION, SCREEN_WIDTH, SCREEN_HEIGHT
from classes.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.screen)
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.screen, "Level1", menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:
                    level = Level(self.screen, "Level2", menu_return, player_score)
                    level_return = level.run(player_score)
                    
                    if level_return:
                        score.save(menu_return, player_score)
            elif menu_return[3]:
                score.show()
            else:
                pygame.quit()
                exit()