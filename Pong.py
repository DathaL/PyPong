import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,360))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50) #insert retro font for score
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


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.active:
                #Background
                self.screen.blit(self.bg_surf,(0,0))

                #Player
                self.screen.blit(self.player_surf,self.left_player_rect)
                self.screen.blit(self.player_surf,self.right_player_rect)

                #Ball
                self.screen.blit(self.ball_surf,self.ball_rect)

            pygame.display.update()
            self.clock.tick(60)

Game().run()