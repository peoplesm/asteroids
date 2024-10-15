import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create random angle for the split
        split_angle = random.uniform(20, 50)

        first_vector = self.velocity.rotate(split_angle)
        second_vector = self.velocity.rotate(-split_angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid.velocity = first_vector * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid.velocity = second_vector * 1.2
