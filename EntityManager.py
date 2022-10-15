import pygame
from entities.Player import *
from entities.Npc import *
from settings.tile_size import *

class EntityManager:
    def __init__(self, group):
        self.group = group
        self.player = Player((3200, 1408), tile_size, self.group)
        self.npcs = [Npc((3200, 1408, tile_size, tile_size * 1.2), "Shinzi", "SHINZI")]
        for npc in self.npcs:
            group.add(npc)
