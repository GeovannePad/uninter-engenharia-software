from datetime import datetime
import pygame

from classes.Const import COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, SCORE_POS
from classes.DBProxy import DBProxy

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.image.load("./assets/ScoreBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def save(self, menu_option, player_score):
        pygame.mixer_music.load(f"./assets/Score.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)
        
        db_proxy = DBProxy("DBScore.db")
        name = ""

        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.score_text(48, "YOU WIN!!", COLOR_YELLOW, SCORE_POS["Title"])

            if menu_option == MENU_OPTION[0]:
                score = player_score[0]
                text = "Player 1 enter your name (4 characters):"
            if menu_option == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = "Enter with the name of the team (4 characters):"
            if menu_option == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = "Player 1 enter your name (4 characters):"
                else:
                    score = player_score[1]
                    text = "Player 2 enter your name (4 characters):"                    

            self.score_text(30, text, COLOR_WHITE, SCORE_POS["EnterName"])
            self.score_text(30, name, COLOR_WHITE, SCORE_POS["Name"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) < 4:
                        db_proxy.save({"name": name, "score": score, "date": get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
        
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load(f"./assets/Score.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.04)

        self.screen.blit(source=self.surface, dest=self.rect)
        self.score_text(48, "TOP 10 SCORE", COLOR_YELLOW, SCORE_POS["Title"])

        db_proxy = DBProxy("DBScore.db")
        list_score = db_proxy.retrive_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f"Name: {name.upper()} | Score: {score:05d} | Date: {date}", COLOR_YELLOW, SCORE_POS[list_score.index(player_score)])

        while True:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surface, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")

    return f"{current_time} - {current_date}"