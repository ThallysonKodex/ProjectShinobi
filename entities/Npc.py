import pygame
from abc import ABC, abstractmethod
from map.konoha import *
from settings.tile_size import *

class Npc(pygame.sprite.Sprite):
    def __init__(self, positioning, npc_folder:str, npc_name:str):
        super().__init__()

        self.path = npc_folder
        self.zed = 2


        self.image = pygame.transform.scale(pygame.image.load(f"graphics/npcs/{self.path}/body/down/0.png").convert_alpha(), (positioning[2], positioning[3]))
        self.rect = self.image.get_rect(topleft = (positioning[0], positioning[1]))

        self.name = npc_name
        self.name_surface = pygame.Surface((100, 40))

        self.h2 = pygame.font.Font("fonts/Pixeled.ttf", 18)
        self.name_render = self.h2.render(self.name, False, (255, 255, 255))




        self.npc_image = f"graphics/npcs/{self.path}/image/0.png"

        self.position = pygame.math.Vector2((positioning[0], positioning[1]))
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def movement(self, dt):
        #if self.direction.magnitude() != 0:
        self.position += self.direction * self.speed * dt
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)

    def multiple_checker(self):

        ls_y = []
        ls_x = []
        for y in range(0, len(world)):
            ls_y.append(int(y * tile_size))
        for i in world:
            for x in range(0, len(i)):
                ls_x.append(int(x * tile_size ))

        self.direction = pygame.math.Vector2((0, 0))
        if int(self.rect.x) not in ls_x:
            self.direction = pygame.math.Vector2((1, 0))
        else:
            self.direction = pygame.math.Vector2((0, 0))

        if int(self.rect.x) not in ls_x:
            self.direction = pygame.math.Vector2((-1, 0))
        else:
            self.direction = pygame.math.Vector2((0, 0))

        if int(self.rect.y) not in ls_y:
            self.direction = pygame.math.Vector2((0, -1))
        else:
            self.direction = pygame.math.Vector2((0, 0))

        if int(self.rect.y) not in ls_y:
            self.direction = pygame.math.Vector2((0, 1))
        else:
            self.direction = pygame.math.Vector2((0, 0))


    def update(self, screen, dt, offset):

        self.movement(dt)
        self.multiple_checker()
        self.name_surface.set_alpha(70)
        screen.blit(self.name_surface, self.name_surface.get_rect(center = self.rect.midtop - offset - (0, 22)))
        screen.blit(self.name_render, self.rect.midtop - offset - (42, 50))

