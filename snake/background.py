import pygame


def draw_polygon_alpha(surface, color, points):
    """ draws the translucent diamonds at given points """
    listx, listy = zip(*points)

    min_x = min(listx)
    min_y = min(listy)
    max_x = max(listx)
    max_y = max(listy)

    target_rect = pygame.Rect(min_x, min_y, (max_x - min_x), (max_y - min_y))
    surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(surf, color, [(x - min_x, y - min_y) for x, y in points])

    surface.blit(surf, target_rect)


def rotate(surface, angle):
    """ make the background image rotate to make a gradient animation """
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1.5)
    rotated_rect = rotated_surface.get_rect(center=(300, 300))
    return rotated_surface, rotated_rect


def background(screen, color):
    """ creates dark translucent tiles pattern for the background """
    for y_shift in range(0, 800, 210):
        for x_shift in range(0, 800, 210):
            draw_polygon_alpha(screen, color, [(-100 + x_shift, 100 + y_shift), (0 + x_shift, 0 + y_shift),
                                               (100 + x_shift, 100 + y_shift), (0 + x_shift, 200 + y_shift)])

            draw_polygon_alpha(screen, color, [(5 + x_shift, -5 + y_shift), (105 + x_shift, -105 + y_shift),
                                               (205 + x_shift, -5 + y_shift), (105 + x_shift, 95 + y_shift)])
