import pygame
from tiles.Processor import *
from map.konoha import *

class SceneManager:
    def __init__(self, group):
        self.konoha = Processor(group)


    def process(self):

        self.konoha.process_map(world)

