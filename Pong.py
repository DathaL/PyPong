import pygame
from sys import exit
from Entities import Player
from Entities import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,360))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("font/Super Mario Bros.ttf", 40) #insert retro font for score
        self.active = True
        #Score
        self.left_score = 0
        self.right_score = 0

        #Images
        self.bg_surf = pygame.image.load("Pictures/background.png").convert()

        #Player
        self.player_surf = pygame.image.load("Pictures/Player.png").convert_alpha()
        self.left_player_rect = self.player_surf.get_rect(center = (30,180))
        self.right_player_rect = self.player_surf.get_rect(center= (610,180))

        #Ball
        self.ball_surf = pygame.image.load("Pictures/Ball.png")
        self.ball_rect = self.ball_surf.get_rect(center=(320,180))

        #Score
        self.score_surf_left = self.font.render(str(self.left_score), False, "White")
        self.score_rect_left = self.score_surf_left.get_rect(midtop = (280,20))
        self.score_surf_right = self.font.render(str(self.right_score),False,"White")
        self.score_rect_right = self.score_surf_right.get_rect(midtop = (360,20))

        #Player
        global player_left
        global player_right
        player_left = Player(self.player_surf,self.left_player_rect)
        player_right = Player(self.player_surf,self.right_player_rect)
        self.movement_left= [False, False]
        self.movement_right = [False, False]
        
        #Ball
        global ball
        ball = Ball(self.ball_surf,self.ball_rect)



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                                
            if self.active:
                keys = pygame.key.get_pressed()

                #Movement
                if keys[pygame.K_w]:
                    player_left.move_up()
                elif keys[pygame.K_s]:
                    player_left.move_down()

                if keys[pygame.K_UP]:
                    player_right.move_up()
                elif keys[pygame.K_DOWN]:
                    player_right.move_down()

                #Background
                self.screen.blit(self.bg_surf,(0,0))
                
                #Players
                self.screen.blit(self.player_surf,self.left_player_rect)
                self.screen.blit(self.player_surf,self.right_player_rect)

                #Score
                self.screen.blit(self.score_surf_left,self.score_rect_left)
                self.screen.blit(self.score_surf_right,self.score_rect_right)

                #Ball
                self.screen.blit(self.ball_surf,self.ball_rect)
                #ball.movement()

            pygame.display.update()
            self.clock.tick(60)




Game().run()