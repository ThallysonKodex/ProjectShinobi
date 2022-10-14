import pygame

import entities.GameObjects
import entities.Player

from SceneManager import *
from EntityManager import *

from AllObjects import *

class Game:
    def __init__(self):
        self.all_objects = AllObjects()

        self.scene_manager = SceneManager(self.all_objects)
        self.scene_manager.process()

        self.entity_manager = EntityManager(self.all_objects)



    def update(self, screen, dt):


        self.all_objects.draw(screen)
        self.all_objects.update(screen, dt)

