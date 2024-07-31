import pygame
import sys
import random

pygame.init()

SW, SH = 800, 800
BLOCK_SIZE = 50
FONT = pygame.font.Font(None, BLOCK_SIZE * 2)  # Use None for default font

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        # Check for self-collision and wall collision
        for square in self.body:
            if self.head.colliderect(square):
                self.dead = False
                break
        if not (0 <= self.head.x < SW and 0 <= self.head.y < SH):
            self.dead = True

        # Reset the snake if dead
        if self.dead:
            self.__init__()  # Reinitialize the snake
            global apple
            apple = Apple()
            return

        # Move the body
        self.body.insert(0, self.head.copy())
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE

        # Remove the last part of the body if the snake hasn't eaten
        self.body.pop()

    def grow(self):
        self.body.append(self.head.copy())

class Apple:
    def __init__(self):
        self.x = (random.randint(0, (SW - BLOCK_SIZE) // BLOCK_SIZE)) * BLOCK_SIZE
        self.y = (random.randint(0, (SH - BLOCK_SIZE) // BLOCK_SIZE)) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.ydir == 0:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir == 0:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir == 0:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()

    screen.fill('black')
    drawGrid()

    apple.update()

    if snake.head.colliderect(apple.rect):
        snake.grow()
        apple = Apple()

    score = FONT.render(f"{len(snake.body)}", True, "white")
    score_rect = score.get_rect(center=(SW / 2, SH / 20))
    screen.blit(score, score_rect)

    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    pygame.display.update()
    clock.tick(10)
