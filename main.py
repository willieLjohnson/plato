#!/Users/waygen/.pyenv/shims/python

import pygame
from pygame.locals import *
import sys
import random

Vector = pygame.math.Vector2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 172)
RED = (255, 0, 172)

HEIGHT = 460
WIDTH = 400
SIZE = (WIDTH, HEIGHT)
ACCELERATION = 0.5
FRICTION = 0.12
FPS = 60
GRAVITY = 0.5

entities = pygame.sprite.Group()
platforms = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((128, 255, 40))
        self.rect = self.surface.get_rect()

        self.position = Vector((10, 360))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
    
    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
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

        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        self.rect.midbottom = self.position
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.velocity.y = -15
        

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((random.randint(50, 100), 12))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(center = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 30)))

    def move(self):
        pass

    def update(self):
        pass

def main():
    pygame.init()
    
    player = Player()
    entities.add(player)

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("GAME")

    running = True

    generate_level()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False

        screen.fill(BLACK)

        for entity in entities:
            screen.blit(entity.surface, entity.rect)
            entity.move()
            entity.update()

        if player.rect.top <= HEIGHT / 3:
            player.position.y += abs(player.velocity.y)
            for platform in platforms:
                if platform.rect.top >= HEIGHT:
                    platform.kill()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

def generate_level():
    for _ in range(random.randint(5, 6)):
        platform = Platform()
        platforms.add(platform)
        entities.add(platform)

if __name__ == "__main__":
    main()
