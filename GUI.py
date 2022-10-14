import pygame
from settings.window import *
from settings.tile_size import *


class GUI():
    def __init__(self, pos, gui_type, buttons_list = None):

        self.gui_type = gui_type

        self.state = 'closed'
        self.size = tile_size
        self.frames()
        self.framei = 7

        self.image = self.frames_normali[self.framei]
        self.rect = self.image.get_rect(center = pos)

        self.button_rects = buttons_list




    def frames(self):
        self.frames_normali = [pygame.transform.scale(pygame.image.load(f"graphics/gui/{self.gui_type}/{framei}.png").convert_alpha(), (780 + (780 / 8), 460 + (460 / 8)))
                              for framei in range(0, 8)]


    def openGUI(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.frames()
