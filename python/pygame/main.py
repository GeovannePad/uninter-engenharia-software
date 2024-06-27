#!/usr/bin/env python3

import pygame

SCREEN_WIDTH = 576
SCREEN_HEIGHT = 324

# Inicializar o Módulo do PyGame
pygame.init()

# Cria uma tela (screen), tudo que for desenhado na tela precisará dessa variável
# Parâmetro `size` especifica o tamanho da janela, passado com tupla.
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surface = pygame.image.load("./assets/background.png").convert_alpha()
player1_surface = pygame.image.load("./assets/player1.png").convert_alpha()

# Obter o retângulo da superfície
bg_rect = bg_surface.get_rect(left=0, top=0)
player1_rect = player1_surface.get_rect(left=100, top=100)

# Desenhar imagem na janela (screen)
screen.blit(source=bg_surface, dest=bg_rect)
screen.blit(source=player1_surface, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo FPS
clock = pygame.time.Clock()

# Carregar música e deixar ela tocando
pygame.mixer_music.load("./assets/fase1.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.03)

while True:
    clock.tick(120) # esse loop está acontecendo 120 vezes por segundo
    #print(f"{clock.get_fps():.0f}") # printar o fps

    screen.blit(source=bg_surface, dest=bg_rect)
    screen.blit(source=player1_surface, dest=player1_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  

    pressed_key = pygame.key.get_pressed()     
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
             
