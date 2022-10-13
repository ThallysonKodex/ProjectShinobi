import pygame
from entities.Player import *
from settings.tile_size import *

class EntityManager:
    def __init__(self, group):
        self.group = group
        self.player = Player((448, 384), tile_size, self.group)
