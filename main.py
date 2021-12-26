#!/Users/waygen/.pyenv/shims/python

import pygame
from pygame.locals import *
import sys
import random

Vector = pygame.math.Vector2

from player import Player
from solid import Solid


class Game():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 172)
    RED = (255, 0, 172)

    SCREEN_HEIGHT = 460
    SCREEN_WIDTH = 400
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    FPS = 60

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.setup()

    def setup(self):
        self.player = Player(self)
        self.entities = pygame.sprite.Group()
        self.solids = pygame.sprite.Group()
        self.entities.add(self.player)
        self.clock = pygame.time.Clock()
        self.generate_level()

    def main(self):
        pygame.init()
        pygame.display.set_caption("plato")

        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.restart()
                    

            self.screen.fill(self.BLACK)

            for entity in self.entities:
                self.screen.blit(entity.surface, entity.rect)
                entity.move()
                entity.update()

            if self.player.rect.top <= self.SCREEN_HEIGHT / 3:
                self.player.position.y += abs(self.player.velocity.y)
                for solid in self.solids:
                    if solid.rect.top >= self.SCREEN_HEIGHT:
                        solid.kill()

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()
        sys.quit()

    def restart(self):
        self.setup()


    def generate_level(self):
        for _ in range(random.randint(5, 6)):
            solid = Solid(self)
            self.solids.add(solid)
            self.entities.add(solid)

    def generate_platform(self):
        while len(self.solids) < 7:
            width = random.randrange(50, 100)
            solid = Solid(self)
            solid.rect.center = (random.randrange(0, self.SCREEN_WIDTH - width), random.randrange(-50, 0))
            self.solids.add(solid)
            self.entities.add(solid)

if __name__ == "__main__":
    game = Game()
    game.main()
