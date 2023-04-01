import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Змейка на Python")

snake_block_size = 10
snake_speed = 15


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([snake_block_size, snake_block_size])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([snake_block_size, snake_block_size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def respawn(self):
        self.rect.x = random.randrange(0, SCREEN_WIDTH - snake_block_size, snake_block_size)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT - snake_block_size, snake_block_size)


snake = Snake()
food = Food()
food.respawn()

all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

clock = pygame.time.Clock()

score = 0

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.rect.x -= snake_block_size
    if keys[pygame.K_RIGHT]:
        snake.rect.x += snake_block_size
    if keys[pygame.K_UP]:
        snake.rect.y -= snake_block_size
    if keys[pygame.K_DOWN]:
        snake.rect.y += snake_block_size

    if snake.rect.x < 0 or snake.rect.x > SCREEN_WIDTH - snake_block_size or snake.rect.y < 0 or snake.rect.y > SCREEN_HEIGHT - snake_block_size:
        game_over = True

    if snake.rect.colliderect(food.rect):
        food.respawn()
        score += 1
        new_block = Snake()
        all_sprites.add(new_block)

    if len(pygame.sprite.spritecollide(snake, all_sprites, False)) > 1:
        game_over = True

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

    clock.tick(snake_speed)

