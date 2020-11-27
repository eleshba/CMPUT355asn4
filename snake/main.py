import pygame
import Snake
import sys
import time
import random

from background import background, rotate


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('apple30.png')
        self.x = 120
        self.y = 120

    def move(self):
        self.x = random.randint(0, 14) * 30
        self.y = random.randint(0, 14) * 30

    def draw(self):

        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


def collision(head_coord, fx, fy):
    if fx <= head_coord[0] < fx + 30:
        if fy <= head_coord[1] < fy + 30:
            return True
    return False


def score(snake):
    score_font = pygame.font.Font("8-BIT WONDER.TTF", 20)
    f_score = score_font.render(f"Score {len(snake.body)}", True, black)
    screen.blit(f_score, (20, 10))


def border(coord, screen_width, head):
    valid = False
    if coord[0] < 0 or coord[0] > (screen_width - head) \
            or coord[1] < 0 or coord[1] > (screen_width - head):
        valid = True
    return valid


def music():
    # pygame.mixer.music.load('Hypnotic-Puzzle3.mp3')
    # pygame.mixer.music.play(-1, 0, 5000)  # -1 is to make it continually play, 4000ms fade-in

    eatsound = pygame.mixer.Sound('UI_Quirky7.wav')
    # to play the sound call eatsound.play()

    return eatsound


def restart():
    font = pygame.font.Font("8-BIT WONDER.TTF", 15)
    respawn = font.render("Press space bar to Respawn or x to Quit", True, (0, 0, 0))
    rect = respawn.get_rect()
    rect.center = screen.get_rect().center
    screen.blit(respawn, rect)
    pygame.display.flip()


def game_loop():
    pygame.init()
    clock = pygame.time.Clock()

    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_width))
    pygame.display.set_caption('Snake Game')
    icon = pygame.image.load('snake.png')
    pygame.display.set_icon(icon)

    eatfx = music()
    img = pygame.image.load("bg.png").convert()

    # colors
    black = (0, 0, 0, 150)
    white = (255, 255, 255, 50)

    angle = 0  # used to rotate image

    FPS = 30
    last_time = time.time()

    food = Food(screen)
    snake = Snake.Snake()

    # game loop
    game_over = False
    while not game_over:

        dt = time.time() - last_time  # time in seconds
        dt *= 30
        last_time = time.time()

        # set background -------------------------------------
        angle += 1 * dt
        screen.fill(white)
        img_rotated, img_rect = rotate(img, angle)
        screen.blit(img_rotated, img_rect)
        score(snake)
        background(screen, black)
        # -------------------------------------------------------

        snake.move_snake()
        snake.draw_snake(screen)
        food.draw()

        if border(snake.head.coordinates, screen_width, snake.body_size[0]):
            game_over = True
            return False

        if snake.istouching():
            game_over = True
            return False

        if collision(snake.head.coordinates, food.x, food.y):
            eatfx.play()
            food.move()
            snake.grow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # LEFT KEY
                    snake.change_dir((-1, 0))
                elif event.key == pygame.K_RIGHT:  # RIGHT KEY
                    snake.change_dir((1, 0))
                elif event.key == pygame.K_UP:  # UP KEY
                    snake.change_dir((0, -1))
                elif event.key == pygame.K_DOWN:  # DOWN KEY
                    snake.change_dir((0, 1))

        pygame.display.flip()
        clock.tick(FPS)


def main():
    global black, screen
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_width))

    black = (0, 0, 0, 150)

    player_alive = game_loop()

    while not player_alive:
        restart()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_alive = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # 'X' KEY
                    player_alive = True
                if event.key == pygame.K_SPACE:  # space bar
                    main()

    pygame.mixer.music.unload()
    pygame.quit()
    quit()
    sys.exit()


main()
