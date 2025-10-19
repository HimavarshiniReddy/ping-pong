import pygame
from game.game_engine import GameEngine

# === Lab 4 Customization Section ===
AUTHOR_NAME = "Himavarshini Reddy"    
WIN_SCORE = 5                         
BALL_SPEED = 7                       
PADDLE_SPEED = 8                      
PLAYER_COLOR = (30, 144, 255)         
ENEMY_COLOR = (220, 20, 60)          
BALL_COLOR = (255, 215, 0)             


# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Ping Pong — Himavarshini Reddy — Lab 4")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT, BALL_SPEED, PADDLE_SPEED, PLAYER_COLOR, ENEMY_COLOR, BALL_COLOR, WIN_SCORE)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()
        
        if engine.left_score >= WIN_SCORE:
            print(f"{AUTHOR_NAME}: Player on the left wins!")
            running = False
        elif engine.right_score >= WIN_SCORE:
            print(f"{AUTHOR_NAME}: Player on the right wins!")
            running = False

        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
