import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
purple = (147, 112, 219)

dis = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

game_over = False

x = 300
y = 300

x_change = 0
y_change = 0

clock = pygame.time.Clock()

while not game_over:
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

    # Change the position each time a key is pressed
    x += x_change
    y += y_change

    dis.fill(white)  # white background
    pygame.draw.rect(dis, purple, [x, y, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()


def main():
    pass


main()
