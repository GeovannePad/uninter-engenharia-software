#/usr/bin/env python3

import random
import pygame
from classes.Enemy import Enemy
from classes.EntityMediator import EntityMediator
from classes.Const import COLOR_CYAN, COLOR_GREEN, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SCREEN_HEIGHT
from classes.EntityFactory import EntityFactory
from classes.Player import Player

class Level:
    def __init__(self, screen, name, menu_option, player_score):
        self.screen = screen
        self.name = name
        self.menu_option = menu_option
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + "Bg"))
        player = EntityFactory.get_entity("Player1")
        player.score = player_score[0]
        self.entity_list.append(player)
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity("Player2")
            player.score = player_score[1]
            self.entity_list.append(player)
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, 3000) 
        pygame.time.set_timer(EVENT_TIMEOUT, 30)     

    def run(self, player_score):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f"./assets/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == "Player1":
                    self.level_text(15, f"Player1 - Health {ent.health} Score: {ent.score}", COLOR_GREEN, (10, 25))
                if ent.name == "Player2":
                    self.level_text(15, f"Player2 - Health {ent.health} Score: {ent.score}", COLOR_CYAN, (10, 45))

            self.level_text(15, f"{self.name} - Timeout: {self.timeout / 1000:.1f}s", COLOR_WHITE, (10, 5))
            self.level_text(15, f"FPS: {clock.get_fps():.0f}", COLOR_WHITE, (10, SCREEN_HEIGHT - 35))
            self.level_text(15, f"Entidades: {len(self.entity_list)}", COLOR_WHITE, (10, SCREEN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                      for ent in self.entity_list:
                          if isinstance(ent, Player) and ent.name == "Player1":
                              player_score[0] = ent.score
                          if isinstance(ent, Player) and ent.name == "Player2":
                              player_score[1] = ent.score
                      return True
                    
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewritter", size=text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surface, dest=text_rect)