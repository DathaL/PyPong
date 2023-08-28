import pygame

class Player:
    def __init__(self,player_surf,player_rect):
        self.player_surf = player_surf
        self.player_rect = player_rect

    def move_up(self):
        if self.player_rect.top > 0:
            self.player_rect.y -= 5

    def move_down(self):
        if self.player_rect.bottom < 360:
            self.player_rect.y += 5

    def ball_collision(self):
        pass