#!/usr/bin/env python3

import random
from classes.Background import Background
from classes.Const import SCREEN_HEIGHT, SCREEN_WIDTH
from classes.Enemy import Enemy
from classes.Player import Player

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
            
            case "Player1":
                return Player("Player1", (10, SCREEN_HEIGHT / 2 - 30))
            
            case "Player2":
                return Player("Player2", (10, SCREEN_HEIGHT / 2 + 30))
            
            case "Enemy1":
                return Enemy("Enemy1", (SCREEN_WIDTH + 15, random.randint(0 + 20, SCREEN_HEIGHT - 20)))
            
            case "Enemy2":
                return Enemy("Enemy2", (SCREEN_WIDTH + 15, random.randint(0 + 20, SCREEN_HEIGHT - 20)))