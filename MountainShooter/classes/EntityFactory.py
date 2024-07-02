#!/usr/bin/env python3

from classes.Background import Background
from classes.Const import SCREEN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []

                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", position))
                    list_bg.append(Background(f"Level1Bg{i}", (SCREEN_WIDTH, 0)))
                return list_bg