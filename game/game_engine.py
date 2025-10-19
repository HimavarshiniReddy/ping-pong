import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

class GameEngine:
    
    def __init__(self, width, height, ball_speed=7, paddle_speed=8,
                 player_color=(30, 144, 255), enemy_color=(220, 20, 60),
                 ball_color=(255, 215, 0), win_score=5):
        self.width = width
        self.height = height
        self.ball_speed = ball_speed
        self.paddle_speed = paddle_speed
        self.player_color = player_color
        self.enemy_color = enemy_color
        self.ball_color = ball_color
        self.win_score = win_score

       
        self.paddle_width = 10
        self.paddle_height = 100

        
        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, self.ball_speed, self.ball_speed, width, height)

       
        self.left_score = 0
        self.right_score = 0

        self.font = pygame.font.SysFont("Arial", 30)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.player.move(-self.paddle_speed, self.height)
        if keys[pygame.K_s]:
            self.player.move(self.paddle_speed, self.height)

    def update(self):
       
        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        
        if self.ball.x <= 0:
            self.right_score += 1
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.left_score += 1
            self.ball.reset()

        
        self.ai.auto_track(self.ball, self.height)

    def render(self, screen):
        
        pygame.draw.rect(screen, self.player_color, self.player.rect())
        pygame.draw.rect(screen, self.enemy_color, self.ai.rect())
        pygame.draw.ellipse(screen, self.ball_color, self.ball.rect())
        pygame.draw.aaline(screen, (255, 255, 255), (self.width // 2, 0), (self.width // 2, self.height))

        
        player_text = self.font.render(str(self.left_score), True, (255, 255, 255))
        ai_text = self.font.render(str(self.right_score), True, (255, 255, 255))
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))
