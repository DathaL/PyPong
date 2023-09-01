import pygame
from random import randint

class Player:
    def __init__(self,player_surf,player_rect):
        self.player_surf = player_surf
        self.player_rect = player_rect

    def move_up(self):
        if self.player_rect.top > 0:
            self.player_rect.y -= 8

    def move_down(self):
        if self.player_rect.bottom < 360:
            self.player_rect.y += 8

class Ball(Player):
    direction ="right"

    def __init__(self, ball_surf, ball_rect):
        self.ball_surf = ball_surf
        self.ball_rect = ball_rect

    def set_angle(self):
        self.angle = randint(2,9)
        self.up_down = randint(0,1)

    def change_up_down(self):
        if self.up_down == 1:
            self.up_down = 0
        else:
            self.up_down = 1

    def movement(self):   
        if self.direction == "right":
            self.ball_rect.x += 5
            if self.up_down:
                self.ball_rect.y -= self.angle
            else:
                self.ball_rect.y += self.angle
        elif self.direction == "left":
            self.ball_rect.x -= 5
            if self.up_down:
                self.ball_rect.y -= self.angle
            else:
                self.ball_rect.y += self.angle

    def change_direc(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
