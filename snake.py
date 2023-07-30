import pygame
import random
import time

pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake attributes
snake_block = 10
snake_speed = 30

# Load the emoji image and resize it to the size of the snake block
beer_img = pygame.image.load("beer.png")
beer_img = pygame.transform.scale(beer_img, (snake_block, snake_block))

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 25)
    rendered_msg = font_style.render(msg, True, color)
    screen.blit(rendered_msg, [screen_width / 6, screen_height / 3])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 25)
    rendered_msg = font_style.render(msg, True, color)
    screen.blit(rendered_msg, [screen_width / 6, screen_height / 3])

def game_loop():
    # Initialize game variables
    game_over = False
    game_close = False

    snake_list = []
    snake_length = 1

    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0

    # Generate random food location
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Game loop
    while not game_over:
        while game_close:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Event handling for game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling for game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        # Boundary conditions
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        screen.fill(black)
        #pygame.draw.rect(screen, white, [food_x, food_y, snake_block, snake_block])
        screen.blit(beer_img, (food_x, food_y))
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        pygame.time.delay(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()

