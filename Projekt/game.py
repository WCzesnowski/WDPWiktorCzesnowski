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


class Player(pygame.sprite.Sprite):
    x_pos = 150
    y_pos = 550
    def __init__(self):
        super(Player, self).__init__()

        x_pos = 150
        y_pos = 550
        y_pos_ducking = 600
        self.Player_duck = False
        self.Player_run = True
        self.Player_jump = False

        self.surf = pygame.Surface((40, 100))
        self.surf.fill((255, 255, 255))
        self.Player_rect = self.image.get_rect()
        self.Player_rect.x = x_pos
        self.Player_rect.y = y_pos

    def move(self, moveinput):
        if self.Player_duck:
            self.duck()

        if self.Player_run:
            self.run()

        if self.Player_jump:
            self.jump()

        if moveinput[pygame.K_UP] and not self.Player_jump:
            self.Player_duck = False
            self.Player_run = False
            self.Player_jump = True
        elif moveinput[pygame.K_DOWN] and not self.Player_jump:
            self.Player_duck = True
            self.Player_run = False
            self.Player_jump = False
        elif not (self.Player_jump or moveinput[pygame.K_DOWN]):
            self.Player_duck = False
            self.Player_run = True
            self.Player_jump = False
    def duck(self):
        pass

    def run(self):
        self.Player_rect = self.image.get_rect()
        self.Player_rect.x = self.x_pos
        self.Player_rect.y= self.y_pos
    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.Player_rect.x, self.Player_rect.y))
        #self.running
        #self.jumping
        #self.ducking
        #self.lower

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
    player = Player()
    game = True
    clock = pygame.time.Clock()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        player.draw(SCREEN)
        player.move(moveinput)
        pygame.display.update()
        screen.fill((40, 30, 40))
        screen.blit(terrain.surf, (0 , 650))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

main()

#def move(self, pressed_keys):



