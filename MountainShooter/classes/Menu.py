import pygame
from classes.Const import SCREEN_WIDTH

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)

        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), (SCREEN_WIDTH / 2, 70))
            pygame.display.flip()
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surface, dest=text_rect)