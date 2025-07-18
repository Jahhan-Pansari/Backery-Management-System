import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird properties
bird_rect = pygame.Rect(50, HEIGHT/2 - 25, 50, 50)
bird_flap = pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap, 200)
bird_gravity = 0.25
bird_movement = 0

# Pipe properties
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 400]
pipe_width = 50

# Game variables
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
game_over_text = pygame.font.Font('freesansbold.ttf', 64)

def draw_bird():
    pygame.draw.rect(WIN, BLACK, bird_rect)

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, random_pipe_pos, pipe_width, HEIGHT - random_pipe_pos)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, random_pipe_pos - 150)
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(WIN, BLACK, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return False
    return True

def score_display():
    score_surface = font.render(f'Score: {int(score)}', True, BLACK)
    score_rect = score_surface.get_rect(center=(WIDTH/2, 50))
    WIN.blit(score_surface, score_rect)

def game_over():
    game_over_surface = game_over_text.render('Game Over', True, BLACK)
    game_over_rect = game_over_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    WIN.blit(game_over_surface, game_over_rect)

# Game loop
running = True
while running:
    WIN.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 7
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == bird_flap:
            bird_movement += 3

    # Bird
    bird_movement += bird_gravity
    bird_rect.centery += bird_movement
    draw_bird()

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Collision
    running = check_collision(pipe_list)

    # Score
    score += 0.01
    score_display()

    # Game Over          
    if not running:
        game_over()

    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(60)
             
pygame.quit()
