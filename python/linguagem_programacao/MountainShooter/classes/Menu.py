#/usr/bin/env python3

import pygame
from classes.Const import COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, COLOR_ORANGE, SCREEN_WIDTH

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.image.load("./assets/MenuBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)

        menu_option = 0

        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, (SCREEN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, (SCREEN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (SCREEN_WIDTH / 2, 200 + 20 * i))
                else: 
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (SCREEN_WIDTH / 2, 200 + 20 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surface, dest=text_rect)