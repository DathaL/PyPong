import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,360))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50) #insert retro font for score

game_active = True

#Score
left_score = 0
right_score = 0

#Images
bg_surf = pygame.image.load("Pictures/background.png").convert()

#Player
player_surf = pygame.image.load("Pictures/Player.png").convert_alpha()
left_player_rect = player_surf.get_rect(center = (30,180))
right_player_rect = player_surf.get_rect(center= (610,180))

#Ball
ball_surf = pygame.image.load("Pictures/Ball.png")
ball_rect = ball_surf.get_rect(center=(320,180))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        #Background
        screen.blit(bg_surf,(0,0))

        #Player
        screen.blit(player_surf,left_player_rect)
        screen.blit(player_surf,right_player_rect)

        #Ball
        screen.blit(ball_surf,ball_rect)

    pygame.display.update()
    clock.tick(60)