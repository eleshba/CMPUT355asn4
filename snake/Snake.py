import Head
from collections import deque
import pygame


class Snake:
    starting_pos = (300, 300)
    body_size = (10, 10)
    purple = (128, 0, 128)

    def __init__(self):
        self.body = deque([])
        self.head = Head.Head(self.starting_pos, (0, 0))

    # draw the snake
    def draw_snake(self, screen):
        self.head.draw_head(screen)
        for body_part in self.body:
            rect = pygame.Rect(body_part, self.body_size)
            pygame.draw.rect(screen, self.purple, rect)

    # changes the velocity vector of the head
    def change_dir(self, new_velocity):
        if (self.head.velocity[0] == 0) and (self.head.velocity[1] == 0):   # starting velocity is zero
            self.head.velocity = new_velocity
        else:  # make sure we cant move in the complete opposite direction
            if self.head.velocity[0] != -(new_velocity[0]):
                if self.head.velocity[1] != -(new_velocity[1]):
                    self.head.velocity = new_velocity

    # Update positions by having each previous node take on the position of the following node
    def move_snake(self):
        # move the body
        if len(self.body) > 0:
            self.body.rotate(1) # move the coordinates over
            self.body.popleft()
            self.body.appendleft(self.head.coordinates)
        # move the head
        self.head.move_head()

    # Grow the snake by appending a new set of coordinates to the body
    def grow(self):
        if not self.body:
            self.body.append(self.head.coordinates)
        else:
            self.body.append(self.body[-1])

    # Detects if the head is in contact with any of the body parts
    def istouching(self):
        for body_part in self.body:
            if self.head.coordinates == body_part:
                return True
        return False
