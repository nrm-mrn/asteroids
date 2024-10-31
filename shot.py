import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, pygame.color.Color(255, 255, 255), self.position, self.radius
        )

    def update(self, dt):
        self.position += dt * self.velocity
