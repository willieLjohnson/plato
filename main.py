import pygame
from pygame.locals import *

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((128, 255, 40))
        self.rect = self.surface.get_rect(center = (10, 420))

        self.position = Vector((10, 385))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
    
    def move(self):
        self.acceleration = Vector(0, 0)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_a]:
            self.acceleration.x = -ACCELERATION
        if keys_pressed[K_d]:
            self.acceleration.x = ACCELERATION

        self.acceleration.x += self.velocity.x * -FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        self.rect.midbottom = self.position
        

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((WIDTH, 20))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(center = (WIDTH / 2, HEIGHT - 10))


def main():
    pygame.init()
    
    platform = Platform()
    player = Player()

    sprites = pygame.sprite.Group()
    sprites.add(platform)
    sprites.add(player)

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("GAME")

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False

        player.move()

        screen.fill(BLACK)

        for sprite in sprites:
            screen.blit(sprite.surface, sprite.rect)

        pygame.display.update()
        # pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
