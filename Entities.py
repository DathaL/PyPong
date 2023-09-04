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

    def start_args(self):
        self.angle = randint(2,7)
        self.speed = 9 - self.angle
        self.up_down = randint(0,1)

    def set_args(self,collidepoint):
        angle_iter = 8
        for dist in range(0,91,9):
            if dist < collidepoint < dist + 9:
                self.angle = angle_iter
            angle_iter -= 1.6
        self.speed = 8 - self.angle

    def change_up_down(self):
        if self.up_down == 1:
            self.up_down = 0
        else:
            self.up_down = 1

    def movement(self):   
        if self.direction == "right":
            self.ball_rect.x += self.speed
            if self.up_down:
                self.ball_rect.y -= self.angle
            else:
                self.ball_rect.y += self.angle
        elif self.direction == "left":
            self.ball_rect.x -= self.speed
            if self.up_down:
                self.ball_rect.y -= self.angle
            else:
                self.ball_rect.y += self.angle

    def change_direc(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
