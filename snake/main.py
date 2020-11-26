import pygame
import Snake
import sys
import time
import random

from background import background, rotate


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('apple.png')
        self.x = 120
        self.y = 120

    def move(self):
        self.x = random.randint(0, 14) * 40
        self.y = random.randint(0, 14) * 40

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


def collision(head_coords, fx, fy):
    if head_coords[0] >= fx and head_coords[0] < fx + 40:
        if head_coords[1] >= fy and head_coords[1] < fy + 40:
            return True
    return False


def score(snake):
    score_font = pygame.font.SysFont("gabriola", 40)
    fscore = score_font.render(f"Your Score: {len(snake.body)}", True, black)
    screen.blit(fscore, (20, 10))


def border(tuple, screen_width, head):
    valid = False
    if tuple[0] < 0 or tuple[0] > (screen_width - head) \
            or tuple[1] < 0 or tuple[1] > (screen_width - head):
        valid = True
    return valid


def music():
    pygame.mixer.music.load('Hypnotic-Puzzle3.mp3')
    pygame.mixer.music.play(-1, 0, 5000)  # -1 is to make it continually play, 4000ms fade-in

    eatsound = pygame.mixer.Sound('UI_Quirky7.wav')
    # to play the sound call eatsound.play()

    return eatsound


def menu():
    # font = pygame.font.SysFont("8-BIT WONDER.TTF", 30)
    pass


def main():
    global x, y, x_change, y_change, screen_width, black, screen

    pygame.init()
    clock = pygame.time.Clock()

    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_width))
    pygame.display.set_caption('Snake Game')
    icon = pygame.image.load('snake.png')
    pygame.display.set_icon(icon)

    # eat = music()

    # images
    light = pygame.image.load("circle.png").convert  # set behind the food for glow effect.
    # screen.blit(light, (food_x_coordinate, food_y_coordinate))
    img = pygame.image.load("bg.png").convert()

    # colors
    black = (0, 0, 0, 150)
    white = (255, 255, 255, 50)

    head = 10  # Snake head size 10 X 10
    angle = 0  # used to rotate image

    FPS = 30
    lasttime = time.time()  # how many secs have passed.

    food = Food(screen)

    # game running loop
    game_over = False
    snake = Snake.Snake()
    while not game_over:

        dt = time.time() - lasttime  # time in seconds
        dt *= 30
        lasttime = time.time()

        angle += 1 * dt

        screen.fill(white)  # white background
        img_rotated, img_rect = rotate(img, angle)
        screen.blit(img_rotated, img_rect)
        score(snake)
        background(screen, black)

        snake.move_snake()
        snake.draw_snake(screen)
        if snake.istouching():
            game_over = True
        # pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # LEFT KEY
                    snake.change_dir((-1, 0))
                elif event.key == pygame.K_RIGHT:  # RIGHT KEY
                    snake.change_dir((1, 0))
                elif event.key == pygame.K_UP:  # UP KEY
                    snake.change_dir((0, -1))
                elif event.key == pygame.K_DOWN:  # DOWN KEY
                    snake.change_dir((0, 1))

        if border(snake.head.coordinates, screen_width, head):
            game_over = True

        food.draw()

        if collision(snake.head.coordinates, food.x, food.y):
            food.move()
            snake.grow()


        pygame.display.flip()

        clock.tick(FPS)

    pygame.mixer.music.unload()
    pygame.quit()
    quit()
    sys.exit()


main()
