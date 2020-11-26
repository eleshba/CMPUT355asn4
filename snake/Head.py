import pygame
import time

class Head:
    black = (0, 0, 0)
    dimension = 10

    def __init__(self, coordinates, velocity):
        self.coordinates = coordinates
        self.velocity = velocity

    def move_head(self,):

        new_x = self.coordinates[0] + self.dimension * self.velocity[0]
        new_y = self.coordinates[1] + self.dimension * self.velocity[1]

        self.coordinates = (new_x, new_y)

    def draw_head(self, screen):
        rect = pygame.Rect(self.coordinates, (self.dimension, self.dimension))
        pygame.draw.rect(screen, self.black, rect)
