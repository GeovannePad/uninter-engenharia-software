#/usr/bin/env python3

import pygame
from classes.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen = screen
        self.name = name
        self.menu_option = menu_option
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                ent.move()

            pygame.display.flip()