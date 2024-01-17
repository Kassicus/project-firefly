import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)

        self.move_speed = 250

        self.image = pygame.Surface([32, 32])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.move_controller()

    def move_controller(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.vel.x = self.move_speed
        elif keys[pygame.K_a]:
            self.vel.x = -self.move_speed
        else:
            self.vel.x = 0

        if keys[pygame.K_s]:
            self.vel.y = self.move_speed
        elif keys[pygame.K_w]:
            self.vel.y = -self.move_speed
        else:
            self.vel.y = 0