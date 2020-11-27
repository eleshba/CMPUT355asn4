import pygame

class Head:
    black = (0, 0, 0)
    dimension = 8

    def __init__(self, coordinates, velocity):
        self.coordinates = coordinates
        self.velocity = velocity

    # change the coordinates in the direction of the velocity
    def move_head(self):
        new_x = self.coordinates[0] + self.dimension * self.velocity[0]
        new_y = self.coordinates[1] + self.dimension * self.velocity[1]

        self.coordinates = (new_x, new_y)

    # draw the snakes head
    def draw_head(self, screen):
        rect = pygame.Rect(self.coordinates, (10, 10))
        pygame.draw.rect(screen, self.black, rect)
