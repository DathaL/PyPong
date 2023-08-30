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
    direction ="right"

    def __init__(self, ball_surf, ball_rect):
        self.ball_surf = ball_surf
        self.ball_rect = ball_rect

    def movement(self):
        if self.direction == "right":
            self.ball_rect.x += 8
        elif self.direction == "left":
            self.ball_rect.x -= 8

    def change_direc(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
