import pygame

class Player:
    def __init__(self,player_surf,player_rect):
        self.player_surf = player_surf
        self.player_rect = player_rect

    def move_up(self):
        if self.player_rect.top > 0:
            self.player_rect.y -= 3

    def move_down(self):
        if self.player_rect.bottom < 360:
            self.player_rect.y += 3

class Ball(Player):
    def __init__(self, ball_surf, ball_rect):
        self.ball_surf = ball_surf
        self.ball_rect = ball_rect

    #def movement(self):
    #    direction = "x"
    #    self.ball_rect.direction += 5

    #def collision(self):
    #    if self.ball_rect.colliderect(self.player_rect):
    #        direction ="y"
