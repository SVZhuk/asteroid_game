import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        spl_vect_right, spl_vect_left = (
            self.velocity.rotate(split_angle),
            self.velocity.rotate(-split_angle),
        )
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        child_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid1.velocity = spl_vect_right * 1.2
        child_asteroid2.velocity = spl_vect_left * 1.2