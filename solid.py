import pygame
import random

Vector = pygame.math.Vector2

class Solid(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.surface = pygame.Surface((random.randint(50, 100), 12))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(center = (random.randint(0, game.SCREEN_WIDTH - 10), random.randint(0, game.SCREEN_HEIGHT - 30)))
        self.game = game

    def move(self):
        pass

    def update(self):
        pass
