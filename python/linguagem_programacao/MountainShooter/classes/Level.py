#/usr/bin/env python3

import random
import pygame
from classes.Const import COLOR_WHITE, EVENT_ENEMY, MENU_OPTION
from classes.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen = screen
        self.name = name
        self.menu_option = menu_option
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))    
        pygame.time.set_timer(EVENT_ENEMY, 4000)       

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f"./assets/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)
                self.level_text(15, f"FPS: {clock.get_fps():.0f}", COLOR_WHITE, (10, 10))
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewritter", size=text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surface, dest=text_rect)