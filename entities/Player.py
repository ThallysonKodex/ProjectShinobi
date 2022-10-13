import pygame

import map.konoha
import settings.tile_size
import settings.window


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.group = group
        self.zed = 0

        self.image = pygame.transform.scale(pygame.image.load("graphics/player/body/down/normal/0.png").convert_alpha(), (size, size * 1.2))
        self.light = pygame.transform.scale(pygame.image.load("graphics/player/body/down/light/0.png").convert_alpha(), (size, size * 1.2))
        self.shadow = pygame.transform.scale(pygame.image.load("graphics/player/body/down/shadow/0.png").convert_alpha(), (size, size * 1.2))

        self.rect = self.image.get_rect(center = pos)

        self.position = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = 120

        self.last_position_x = 'right'
        self.last_position_y = 'down'


    def movement(self, dt):
        if self.direction.magnitude() != 0:
            self.position += self.direction * self.speed * dt
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def input(self):
        kb = pygame.key.get_pressed()
        if kb[pygame.K_w]:
            if self.direction.magnitude() == 0:
                self.last_position_y = 'up'
                self.direction.y = -1
        elif kb[pygame.K_s]:
            if self.direction.magnitude() == 0:
                self.last_position_y = 'down'
                self.direction.y = 1
        elif kb[pygame.K_d]:
            if self.direction.magnitude() == 0:
                self.last_position_x = 'right'
                self.direction.x = 1
        elif kb[pygame.K_a]:
            if self.direction.magnitude() == 0:
                self.last_position_x = 'left'
                self.direction.x = -1

    def multiple_checker(self):
        ls_y = []
        ls_x = []
        for y in range(0, int(len(map.konoha.world))):
            ls_y.append(int(y * settings.tile_size.tile_size))
        for i in map.konoha.world:
            for x in range(0, int(len(i))):
                ls_x.append(int(x * settings.tile_size.tile_size))


        if self.direction.x == 1 and self.last_position_x == "right":
            if int(self.position.x) not in ls_x:
                self.direction = pygame.math.Vector2((1, 0))
            else:
                self.direction = pygame.math.Vector2((0, 0))
        if self.direction.x == -1 and self.last_position_x == "left":
            if int(self.position.x) not in ls_x:
                self.direction = pygame.math.Vector2((-1, 0))
            else:
                self.direction = pygame.math.Vector2((0, 0))
        if self.direction.y == -1 and self.last_position_y == "up":
            if int(self.position.y) not in ls_y:
                self.direction = pygame.math.Vector2((0, -1))
            else:
                self.direction = pygame.math.Vector2((0, 0))
        if self.direction.y == 1 and self.last_position_y == "down":
            if int(self.position.y) not in ls_y:
                self.direction = pygame.math.Vector2((0, 1))
            else:
                self.direction = pygame.math.Vector2((0, 0))

    def update(self, dt):
        print(int(self.position.y))
        self.multiple_checker()
        self.input()
        self.movement(dt)






