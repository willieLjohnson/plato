import pygame
from pygame.locals import *

Vector = pygame.math.Vector2

ACCELERATION = 0.5
FRICTION = 0.12
FPS = 60
GRAVITY = 0.5

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((128, 255, 40))
        self.rect = self.surface.get_rect()

        self.position = Vector((10, 360))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.game = game
    
    def update(self):
        hits = pygame.sprite.spritecollide(self, self.game.solids, False)
        if hits and self.velocity.y > 0:
            self.position.y = hits[0].rect.top + 1
            self.velocity.y = 0
    
    def move(self):
        self.acceleration = Vector(0, GRAVITY)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_a]:
            self.acceleration.x = -ACCELERATION
        if keys_pressed[K_d]:
            self.acceleration.x = ACCELERATION
        if keys_pressed[K_SPACE]:
            self.jump()


        self.acceleration.x += self.velocity.x * -FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x > self.game.SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = self.game.SCREEN_WIDTH
        self.rect.midbottom = self.position
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, self.game.solids, False)
        if hits:
            self.velocity.y = -15
        