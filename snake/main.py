import pygame
import Snake


def border(x, y, screen_width, head):
    valid = False
    if x < 0 or x > (screen_width - head) \
            or y < 0 or y > (screen_width - head):
        valid = True
    return valid


def main():
    global x, y, x_change, y_change

    pygame.init()
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_width))
    pygame.display.set_caption('Snake Game')

    icon = pygame.image.load('snake.png')
    pygame.display.set_icon(icon)

    # eating SFX
    eatsound = pygame.mixer.Sound('UI_Quirky7.wav')
    # to play the sound call eatsound.play()

    music = pygame.mixer.music.load('Hypnotic-Puzzle3.mp3')

    # -1 is to make it continually play, 4000ms fade-in
    pygame.mixer.music.play(-1, 0, 4000)

    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()
    white = (255, 255, 255)
    purple = (128, 0, 128)

    head = 10  # Snake head rect size 10 X 10

#    x = 300
#    y = 300
#    x_change = 0
#    y_change = 0

    game_over = False
    snake = Snake.Snake()
    while not game_over:
        screen.fill(white)  # white background
        snake.move_snake()
        snake.draw_snake(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # LEFT KEY
                    snake.change_dir((-1,0))
                elif event.key == pygame.K_RIGHT:  # RIGHT KEY
                    snake.change_dir((1,0))
                elif event.key == pygame.K_UP:  # UP KEY
                    snake.change_dir((0,-1))
                elif event.key == pygame.K_DOWN:  # DOWN KEY
                    snake.change_dir((0,1))
                elif event.key == pygame.K_SPACE:
                    snake.grow()

        #if border(x, y, screen_width, head):
        #   game_over = True


        # Change the position each time a key is pressed
        #x += x_change
        #y += y_change

        #pygame.draw.rect(screen, purple, [x, y, head, head])

        clock.tick(30)

    pygame.mixer.music.unload()
    pygame.quit()
    quit()


main()
