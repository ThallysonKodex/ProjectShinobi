import pygame

import entities.GameObjects
import entities.Player

from SceneManager import *
from EntityManager import *

class AllObjects(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        # For each sprite in self.sprites() minus any classes that are "Player" or "GameObjects", draw them.
        # *(Draw MAP only)*
        for sprite in sorted([ins for ins in self.sprites() if ins.__class__ != Player and entities.GameObjects.GameObjects], key = lambda a: a.zed):
            screen.blit(sprite.image, sprite.rect)


        for sprite in sorted([ins for ins in self.sprites() if ins.__class__ == Player and entities.GameObjects.GameObjects], key= lambda a: a.rect.y):
            screen.blit(sprite.image, sprite.rect)

        for sprite in [ins for ins in self.sprites() if ins.__class__ == Player]:
            screen.blit(sprite.__getattribute__('shadow'), sprite.rect)
            screen.blit(sprite.__getattribute__('light'), sprite.rect)

    def get_all(self):
        for sprite in sorted(self.sprites(), key = lambda a: a.zed):
            print(sprite.rect.x)



class Game:
    def __init__(self):
        self.all_objects = AllObjects()

        self.scene_manager = SceneManager(self.all_objects)
        self.scene_manager.process()

        self.entity_manager = EntityManager(self.all_objects)



    def update(self, screen, dt):


        self.all_objects.draw(screen)
        self.all_objects.update(dt)

