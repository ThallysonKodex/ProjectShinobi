import pygame
from settings.tile_size import *
from tiles.grass_tiles import *
from entities.Player import *
from settings.window import *

class Processor:
    def __init__(self, group):
        self.group = group



    def process_map(self, map):



        for row_index, row in enumerate(map):
            for column_index, column in enumerate(row):
                if column == "H":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassMiddleMid((x, y), tile_size, self.group)

                if column == "I":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassTopLeft((x, y), tile_size, self.group)
                    
                if column == "J":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassTopMid((x, y), tile_size, self.group)
                    
                if column == "K":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassTopRight((x, y), tile_size, self.group)
                    
                if column == "E":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassEdgeTopRight((x, y), tile_size, self.group)
                    
                if column == "D":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassBottomMid((x, y), tile_size, self.group)
                    
                if column == "F":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassBottomRight((x, y), tile_size, self.group)
                    
                if column == "B":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassEdgeBottomLeft((x, y), tile_size, self.group)
                    
                if column == "C":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassBottomLeft((x, y), tile_size, self.group)
                    
                if column == "A":
                    x = column_index * tile_size - 35
                    y = row_index * tile_size - 25
                    tile = GrassEdgeTopLeft((x, y), tile_size, self.group)
                    
