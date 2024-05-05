import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta untuk ukuran layar
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Kecepatan dan ukuran ular
snake_size = 10
snake_speed = 10

# Mengatur judul jendela
pygame.display.set_caption('Game Ular')

# Fungsi untuk menggambar ular
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_size, snake_size])

# Fungsi untuk menampilkan makanan
def draw_food(food_x, food_y):
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

# Main loop
def game_loop():
    game_over = False
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_size
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
            game_over = True

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        screen.fill(WHITE)
        draw_food(food_x, food_y)
        draw_snake(snake_list)

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()