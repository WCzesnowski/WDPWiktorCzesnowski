#Sidescroller z urozmaiceniami (downwards_dash,double jump platform/powerup, shooting)
import pygame
import time
pygame.init()
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

WIDTH = 1100
HEIGHT = 850
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("SideScroller")
pressed_keys = pygame.key.get_pressed()

x_pos = 150
y_pos = 550
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((40, 100))
        self.surf.fill((255, 255, 255))
        self.playerx = x_pos
        self.playery = y_pos
        self.rect = pygame.Rect(self.playerx, self.playery, 40 , 100)
        #self.running
        #self.jumping
        #self.ducking
        #self.lower

player = Player()

#class Obstacle(pygame.sprite.Sprite):
 #   def __init__(self):
  #      super(Obstacle, self).__init__()

class Terrain(pygame.sprite.Sprite):
    def __init__(self):
        super(Terrain, self).__init__()
        self.surf = pygame.Surface((WIDTH, 450))
        self.surf.fill((0, 120, 30))

terrain = Terrain()



def main():
    game = True
    y_pos = 550
    x_pos = 150
    #player = figure
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False


        pygame.display.update()
        screen.fill((40, 30, 40))
        screen.blit(terrain.surf, (0 , 650))
        screen.blit(player.surf, (x_pos,y_pos))
        pygame.display.flip()

main()

#def move(self, pressed_keys):



