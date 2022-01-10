#Sidescroller z urozmaiceniami (downwards_dash,double jump platform/powerup, shooting)
import pygame
import time
pygame.init()

WIDTH = 850
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("SideScroller")
pressed_keys = pygame.key.get_pressed()


class Player(pygame.sprite.Sprite):
    x_pos=50
    y_pos=350

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100,50))
        self.surf.fill((255,255,255))
        self.running
        self.jumping
        self.ducking
        self.lower


def main():
    game = True
    screen.fill((40, 30, 40))
    surf = pygame.Surface((50, 50))
    surf.fill((255, 255, 255))
    screen.blit(surf, (WIDTH / 2, HEIGHT / 2))
    pygame.display.flip()
    #player = figure
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        pygame.display.update()

#def move(self, pressed_keys):



main()

