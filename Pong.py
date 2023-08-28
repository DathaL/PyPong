import pygame
from sys import exit
from Entities import Player

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
        self.bg_surf = pygame.image.load("PyPong/Pictures/background.png").convert()

        #Player
        self.player_surf = pygame.image.load("PyPong/Pictures/Player.png").convert_alpha()
        self.left_player_rect = self.player_surf.get_rect(center = (30,180))
        self.right_player_rect = self.player_surf.get_rect(center= (610,180))

        #Ball
        self.ball_surf = pygame.image.load("PyPong/Pictures/Ball.png")
        self.ball_rect = self.ball_surf.get_rect(center=(320,180))

        global player_left
        global player_right
        player_left = Player(self.player_surf,self.left_player_rect)
        player_right = Player(self.player_surf,self.right_player_rect)
        
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            player_left.move_up()
                        if event.key == pygame.K_s:
                            player_left.move_down()
                        if event.key == pygame.K_UP:
                            player_right.move_up()
                        if event.key == pygame.K_DOWN:
                            player_right.move_down()

            if self.active:
                #Background
                self.screen.blit(self.bg_surf,(0,0))
                
                #Players
                self.screen.blit(self.player_surf,self.left_player_rect)
                self.screen.blit(self.player_surf,self.right_player_rect)

            pygame.display.update()
            self.clock.tick(60)




Game().run()