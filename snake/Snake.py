import Head
from collections import deque
import pygame

class Snake:
    starting_pos = (300, 300)
    body_size = (10, 10)
    purple = (128, 0, 128)

    def __init__(self):
        self.body = deque([])
        self.head = Head.Head(self.starting_pos, (1, 0))

    def draw_snake(self, screen):
        self.head.draw_head(screen)
        for bodypart in self.body:
            rect = pygame.Rect(bodypart, self.body_size)
            pygame.draw.rect(screen, self.purple, rect)

    def change_dir(self, new_velocity):
        if self.head.velocity[0] != -(new_velocity[0]):
            if self.head.velocity[1] != -(new_velocity[1]):
                self.head.velocity = new_velocity

    def move_snake(self):
        # move the body
        if len(self.body) > 0:
            self.body.rotate(1)
            self.body.popleft()
            self.body.appendleft(self.head.coordinates)
        # move the head
        self.head.move_head()

    def grow(self):
        if not self.body:
            self.body.append(self.head.coordinates)
        else:
            self.body.append(self.body[-1])
