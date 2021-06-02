import sys
import pygame


class Bob(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_color = pygame.Color(128, 128, 128)

bob = Bob(200, 200, 100, 100, (0, 0, 0))

bob_group = pygame.sprite.Group()
bob_group.add(bob)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    pygame.display.flip()
    bob_group.draw(screen)
    clock.tick(60)
