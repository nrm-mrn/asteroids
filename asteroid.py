import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, pygame.color.Color(255, 255, 255), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_spawn_ang_1 = self.velocity.rotate(angle)
        new_spawn_ang_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_spawn_1.velocity = new_spawn_ang_1 * 1.2
        new_spawn_2.velocity = new_spawn_ang_2 * 1.2
