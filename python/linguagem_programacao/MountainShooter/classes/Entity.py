#!/usr/bin/env python3

from abc import ABC, abstractmethod
import pygame
from classes.Const import ENTITY_HEALTH

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surface = pygame.image.load("./assets/" + name + ".png").convert_alpha()
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):
        pass