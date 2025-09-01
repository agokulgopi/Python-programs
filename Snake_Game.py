import pygame
import sys
import random

#from pygame.examples.go_over_there import running

#from main import screen, WHITE

pygame.init() #initialize pygame

#screen setup
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20 #size of snake block
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

#colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0 ,0)

#clock
clock = pygame.time.Clock()
FPS = 10 #speed of the snake

#Font for score
font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def message(text, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, [x, y])

def game_loop():
    #snake starting position
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_dx = 0
    snake_dy = 0
    snake_list = []
    snake_length = 1

    #food position
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y =random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #key controls
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a] and snake_dx == 0:
                    snake_dx = -BLOCK_SIZE
                    snake_dy = 0
                if event.key in [pygame.K_RIGHT, pygame.K_d] and snake_dx == 0:
                    snake_dx = BLOCK_SIZE
                    snake_dy = 0
                if event.key in [pygame.K_UP, pygame.K_w] and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = -BLOCK_SIZE
                if event.key in [pygame.K_DOWN, pygame.K_s] and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = BLOCK_SIZE

        #update snake position
        snake_x += snake_dx
        snake_y += snake_dy

        # create snake rect for collision check
        snake_rect = pygame.Rect(snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE)

        #check boundaries (Game over)
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            running = False

        #fill background
        screen.fill(WHITE)

        #draw Food
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        food_rect = pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE)

        #snake body
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        #check if snake hits itself
        for block in snake_list[:-1]:
            if block == snake_head:
                running = False

        #draw snake
        draw_snake(snake_list)

        #check food collision
        if snake_rect.colliderect(food_rect):
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1
            score += 1

        #show score
        message(f"Score: {score}", BLACK, 10, 10)

        #update display
        pygame.display.flip()

        #control speed
        clock.tick(FPS)

    #Game over screen
    screen.fill(WHITE)
    message("Game over! Press R to Restart or Q to Quit", RED, WIDTH//6, HEIGHT//3)
    pygame.display.flip()

    #wait for restart/quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    waiting = False
                if event.key == pygame.K_r:
                    game_loop()

game_loop()