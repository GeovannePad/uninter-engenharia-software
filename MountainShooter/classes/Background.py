#!/usr/bin/env python3

from classes.Const import ENTITY_SPEED, SCREEN_WIDTH
from classes.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH
