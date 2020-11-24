import pygame
import sys
import time

from background import background, rotate


def border(x, y, screen_width, head):
    valid = False
    if x < 0 or x > (screen_width - head) \
            or y < 0 or y > (screen_width - head):
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
    global x, y, x_change, y_change

    pygame.init()
    clock = pygame.time.Clock()

    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_width))
    pygame.display.set_caption('Snake Game')
    icon = pygame.image.load('snake.png')
    pygame.display.set_icon(icon)

    eat = music()

    # images
    light = pygame.image.load("circle.png").convert  # set behind the food for glow effect.
    # screen.blit(light, (food_x_coordinate, food_y_coordinate))
    img = pygame.image.load("bg.png").convert()

    # colors
    black = (0, 0, 0, 150)
    white = (255, 255, 255, 50)

    head = 12  # Snake head size 10 X 10

    # starting position for snake
    x = 300
    y = 300

    # change in snakes position
    x_change = 0
    y_change = 0

    angle = 0  # used to rotate image

    FPS = 30
    lasttime = time.time()  # how many secs have passed.

    # game running loop
    game_over = False
    while not game_over:
       
        dt = time.time() - lasttime     # time in seconds
        dt *= 30
        lasttime = time.time()

        angle += 1 * dt
        screen.fill((255, 255, 255))
        img_rotated, img_rect = rotate(img, angle)

        screen.blit(img_rotated, img_rect)
        background(screen, black)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # LEFT KEY
                    x_change = -5
                    y_change = 0
                elif event.key == pygame.K_RIGHT:  # RIGHT KEY
                    x_change = 5
                    y_change = 0
                elif event.key == pygame.K_UP:  # UP KEY
                    y_change = -5
                    x_change = 0
                elif event.key == pygame.K_DOWN:  # DOWN KEY
                    y_change = 5
                    x_change = 0

        if border(x, y, screen_width, head):
            game_over = True

        # Change the position each time a key is pressed
        x += x_change * dt
        y += y_change * dt

        pygame.draw.rect(screen, white, [x, y, head, head])
        pygame.display.flip()
        clock.tick(FPS)

    pygame.mixer.music.unload()
    pygame.quit()
    quit()
    sys.exit()


main()
