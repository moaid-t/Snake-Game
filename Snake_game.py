import pygame
import random

pygame.font.init()
pygame.init()

width, height = 550, 500
screen = pygame.display.set_mode([width, height])


# class
class Food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, [220, 220, 220], [self.x, self.y, 20, 20])

    def change_loc(self, width, height):
        self.x = random.randint(1, width - 20)
        self.y = random.randint(1, height - 20)


class Snake(object):
    part = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Snake.part.append(self)

    def draw(self, screen):
        for i in range(len(Snake.part)):
            if i == 0:
                pygame.draw.rect(screen, [196, 96, 196], [Snake.part[i].x, Snake.part[i].y, 20, 20])
            else:
                pygame.draw.rect(screen, [196, 96, 196], [Snake.part[i].x, Snake.part[i].y, 20, 20])

    def mov_X(self, var):
        for i in range(len(Snake.part) - 1, -1, -1):
            if i == 0:
                Snake.part[0].x += var
                break
            Snake.part[i].x = Snake.part[i - 1].x

    def eat_self(self):
        for i in range(1, len(Snake.part)):
            if Snake.part[i].x == snake.get_headX() and Snake.part[i].y == snake.get_headY():
                return True

    def mov_Y(self, var):
        for i in range(len(Snake.part) - 1, -1, -1):
            if i == 0:
                Snake.part[0].y += var
                break
            Snake.part[i].y = Snake.part[i - 1].y

    def get_headX(self):
        return Snake.part[0].x

    def get_headY(self):
        return Snake.part[0].y


# screen var
run = True
FBS = 60
clock = pygame.time.Clock()

# lose var
lose = False
lose_font = pygame.font.SysFont('comicsans', 40)

# snake var
snake = Snake(100, 100)
snake_vel = 2
snake_x = 0
snake_y = 0

# food var
food = Food(random.randrange(5, 300), random.randrange(5, 300))


# function
def eat_food():
    x = snake.get_headX() - food.x
    y = snake.get_headY() - food.y
    if (x >= -10 and x <= 10) and (y >= -10 and y <= 10):
        return True
    else:
        return False


# run loop
def draw():
    screen.fill([22, 33, 44])
    lose_label = lose_font.render(' -YOU LOSE- ', 1, [225, 225, 225])

    # draw in screen
    if lose:
        screen.blit(lose_label, [width / 2 - lose_label.get_width() / 2, height / 2])

    food.draw(screen)
    snake.draw(screen)

    pygame.display.update()


while run:
    clock.tick(FBS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and snake_x == 0:
                snake_x = snake_vel
                snake_y = 0
            if event.key == pygame.K_a and snake_x == 0:
                snake_x = -snake_vel
                snake_y = 0
            if event.key == pygame.K_w and snake_y == 0:
                snake_x = 0
                snake_y = -snake_vel
            if event.key == pygame.K_s and snake_y == 0:
                snake_x = 0
                snake_y = snake_vel

    snake.mov_X(snake_x)
    snake.mov_Y(snake_y)

    if snake.get_headX() < 0 or snake.get_headX() + 20 > width:
        lose = True
    if snake.get_headY() < 0 or snake.get_headY() + 20 > height:
        lose = True
    if snake.eat_self():
        lose = True

    if eat_food():
        food.change_loc(width, height)
        if snake_x > 0:
            Snake(snake.get_headX() - 20, snake.get_headY())
        elif snake_x < 0:
            Snake(snake.get_headX() + 20, snake.get_headY())
        if snake_y > 0:
            Snake(snake.get_headX(), snake.get_headY() - 20)
        elif snake_y < 0:
            Snake(snake.get_headX(), snake.get_headY() + 20)

    draw()
