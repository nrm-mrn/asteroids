import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collide(self, obj) -> bool:
        distance = self.position.distance_to(obj.position)
        min_dist = self.radius + obj.radius
        if distance <= min_dist:
            return True
        return False

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
