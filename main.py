import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 172)
RED = (255, 0, 172)

HEIGHT = 460
WIDTH = 400
SIZE = (WIDTH, HEIGHT)
ACC = 0.5
FRIC = 0.12
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center = (10, 420))
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (WIDTH / 2, HEIGHT - 10))


def main():
    pygame.init()
    vec = pygame.math.Vector2
    
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
    
        screen.fill(BLACK)

        for sprite in sprites:
            screen.blit(sprite.surf, sprite.rect)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
