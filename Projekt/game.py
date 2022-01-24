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
    velocity = 3
    def __init__(self):

        super(Player, self).__init__()
        self.surf = pygame.Surface((40, 100))
        self.surf.fill((255, 255, 255))
        self.x = self.x_pos
        self.y = self.y_pos
        self.Player_rect = pygame.Rect(self.x, self.y, 40 , 100)
        self.vel = self.velocity
        self.inAir = False
        #self.running
        #self.jumping
        #self.ducking
        #self.lower

    def move(self):
        inp = pygame.key.get_pressed()
        if inp[K_UP] and self.inAir == False:
            for i in range(self.y_pos, 300 , -1):
                self.y_pos = i
        if inp[K_DOWN]:
            self.vel = 15
            if self.y_pos == 550:
                self.vel = 3


    def draw(self):
        screen.blit(self.surf, (self.x_pos, self.y_pos))

    def stance(self):
        if self.y_pos > 550 and self.y_pos < 560:
            self.y_pos = 550
        if self.y_pos == 550:
            self.inAir = False
        if self.y_pos < 550:
            self.inAir = True
            self.y_pos += self.vel






#class Obstacle(pygame.sprite.Sprite):
 #   def __init__(self):
  #      super(Obstacle, self).__init__()

class Terrain(pygame.sprite.Sprite):
    def __init__(self):
        super(Terrain, self).__init__()
        self.surf = pygame.Surface((WIDTH, 450))
        self.surf.fill((0, 120, 30))

class Obstacle(pygame.sprite.Sprite):
    ob_x = 1000
    ob_y = 550
    def __init__(self):
        super(Obstacle, self).__init__()
        self.x = self.ob_x
        self.y = self.ob_y
        self.surf = pygame.Surface((40, 100))
        self.surf.fill((255, 255, 255))
        self.Obstacle_rect = pygame.Rect(self.x, self.y, 40, 100)

    #def spawn(self):
        #spawn = True
        #i = 0
        #while spawn == True:
            #pygame.time.delay(30)
            #i += 0.5
        #if i == 20:
            #screen.blit(self.area, (self.x, self.y))






def main():
    game = True
    terrain = Terrain()
    player = Player()
    obstacle = Obstacle()
    clock = pygame.time.Clock()
    #player = figure
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        screen.fill((40, 30, 40))
        #obstacle.spawn()
        player.stance()
        player.draw()
        player.move()
        screen.blit(terrain.surf, (0 , 650))
        pygame.display.flip()
        clock.tick(60)

main()

