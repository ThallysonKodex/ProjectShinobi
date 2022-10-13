import pygame

class GrassBottomLeft(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/bottomleft.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassBottomMid(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/bottommid.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassBottomRight(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/bottomright.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassEdgeBottomLeft(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/edgebottomL.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassEdgeBottomRight(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/edgebottomR.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassEdgeTopLeft(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/edgeleft.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassEdgeTopRight(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/edgeright.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassMiddleLeft(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/middleleft.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassMiddleMid(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/middlemid.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2
class GrassMiddleRight(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/middleright.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2

class GrassTopLeft(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/topleft.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2

class GrassTopMid(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/topmid.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2

class GrassTopRight(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load("graphics/world/tiles/grass/topright.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(center = pos)
        self.zed = 2