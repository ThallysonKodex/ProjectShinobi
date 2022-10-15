from animation.animation import *
import pygame
import Npc

class Gui(pygame.sprite.Sprite):
    def __init__(self, rect, scale, npc:Npc.Npc = None):
        super().__init__()

        if scale == 'normal':
            self.image = pygame.transform.scale(pygame.image.load("graphics/gui/size/0.png"), (rect[2], rect[3]))
        if scale == 'dialogue':
            self.image = pygame.image.load("graphics/gui/size/1.png")
        self.rect = self.image.get_rect(topleft = (rect[0], rect[1]))
        if npc.__class__ == Npc:
            self.npc_image = npc.npc_image
        elif npc.__class__ != Npc:
            print("Argument 3 has to be NPC class")