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
        self.angle = randint(1,3)
        self.up_down = randint(0,1)
        self.speed = 5 - self.angle

    def set_args(self,collidepoint):
        count = 1
        angle_iter = 4.0
        for dist in range(0,91,9):
            if count <= 4:
                angle_iter -= 0.8
                self.up_down = 1
            elif count > 4:
                angle_iter += 0.8
                self.up_down = 0
            count += 1
            if dist < collidepoint < dist + 9:
                self.angle = angle_iter
                print(f"Count: {count}")
                break
        self.speed = 8 - self.angle
        print(f"Speed: {self.speed}")
        print(f"Angle: {self.angle}")
        print(f"up or down: {self.up_down}")

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

    def direc_right(self):
        self.direction = "right"
    
    def direc_left(self):
        self.direction = "left"