import pygame
from settings.tile_size import *
from tiles.grass_tiles import *
from entities.Player import *
from settings.window import *

class Processor:
    def __init__(self, group):
        self.group = group



    def process_map(self, map, map2 = None, map3 = None, map4 = None):



        for row_index, row in enumerate(map):
            for column_index, column in enumerate(row):
                if column == "H":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassMiddleMid((x, y), tile_size, self.group)

                if column == "I":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassTopLeft((x, y), tile_size, self.group)
                    
                if column == "J":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassTopMid((x, y), tile_size, self.group)
                    
                if column == "K":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassTopRight((x, y), tile_size, self.group)
                    
                if column == "E":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassEdgeTopRight((x, y), tile_size, self.group)
                    
                if column == "D":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassBottomMid((x, y), tile_size, self.group)
                    
                if column == "F":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassBottomRight((x, y), tile_size, self.group)
                    
                if column == "B":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassEdgeBottomLeft((x, y), tile_size, self.group)
                    
                if column == "C":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassBottomLeft((x, y), tile_size, self.group)
                    
                if column == "A":
                    x = column_index * tile_size - 10
                    y = row_index * tile_size - 100
                    tile = GrassEdgeTopLeft((x, y), tile_size, self.group)
                    
