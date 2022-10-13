import pygame

import map.konoha
import settings.tile_size
import settings.window


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.group = group
        self.zed = 0
        self.size = size

        self.frame = 0
        self.sprite_direction = 'down'
        self.frames(self.sprite_direction)

        self.image = self.frames_normal[self.frame]
        self.light = self.frames_light[self.frame]
        self.shadow = self.frames_shadow[self.frame]
        self.custom = []

        self.rect = self.image.get_rect(center = pos)

        self.position = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = 120

        self.last_position_x = 'right'
        self.last_position_y = 'down'

    def frames(self, sprite_direction):
        self.frames_normal = [pygame.transform.scale(pygame.image.load(f"graphics/player/body/{sprite_direction}/normal/{frame}.png").convert_alpha(), (self.size, self.size * 1.2))
                              for frame in range(7)]
        self.frames_shadow = [pygame.transform.scale(pygame.image.load(f"graphics/player/body/{sprite_direction}/shadow/{frame}.png").convert_alpha(), (self.size, self.size * 1.2))
                              for frame in range(7)]
        self.frames_light = [pygame.transform.scale(pygame.image.load(f"graphics/player/body/{sprite_direction}/light/{frame}.png").convert_alpha(), (self.size, self.size * 1.2))
                             for frame in range(7)]

    def animation(self, dt):
        if self.direction.magnitude() != 0:
            self.frame += 1 * (self.speed / 10) * dt
            if self.frame >= 7:
                self.frame = 0
            self.image = pygame.transform.scale(self.frames_normal[int(self.frame)], (self.size, self.size* 1.2))
            self.shadow = pygame.transform.scale(self.frames_shadow[int(self.frame)], (self.size, self.size* 1.2))
            self.light = pygame.transform.scale(self.frames_light[int(self.frame)], (self.size, self.size* 1.2))
        else:
            self.frame = 0
        self.image = pygame.transform.scale(self.frames_normal[int(self.frame)], (self.size, self.size* 1.2))
        self.shadow = pygame.transform.scale(self.frames_shadow[int(self.frame)], (self.size, self.size* 1.2))
        self.light = pygame.transform.scale(self.frames_light[int(self.frame)], (self.size, self.size* 1.2))

    def movement(self, dt):
        if self.direction.magnitude() != 0:
            self.position += self.direction * self.speed * dt
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def input(self):
        kb = pygame.key.get_pressed()
        if kb[pygame.K_w]:
            if self.direction.magnitude() == 0:
                self.sprite_direction = 'up'
                self.last_position_y = 'up'
                self.direction.y = -1

        elif kb[pygame.K_s]:
            if self.direction.magnitude() == 0:
                self.sprite_direction = 'down'
                self.last_position_y = 'down'
                self.direction.y = 1
        elif kb[pygame.K_d]:
            if self.direction.magnitude() == 0:
                self.sprite_direction = 'right'
                self.last_position_x = 'right'
                self.direction.x = 1
        elif kb[pygame.K_a]:
            if self.direction.magnitude() == 0:
                self.sprite_direction = 'left'
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
        self.movement(dt)

        self.frames(self.sprite_direction)
        self.animation(dt)

        self.multiple_checker()
        self.input()








