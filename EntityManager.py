import pygame
from entities.Player import *
from settings.tile_size import *

class EntityManager:
    def __init__(self, group):
        self.group = group
        self.player = Player((WINDOW_W / 2, WINDOW_H / 2), tile_size, self.group)
