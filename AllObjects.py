import pygame
from settings.window import *
from entities.Player import *
from entities.GameObjects import *
class AllObjects(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

    def draw(self, screen):

        # Gets all sprites that class is equal to player.
        for sprite in [ins for ins in self.sprites() if ins.__class__ == Player]:
            # Sets the offset attribute x and y position according to the player position x and y
            self.offset.x = sprite.rect.x - WINDOW_W / 2
            self.offset.y = sprite.rect.y - WINDOW_H / 2

        # Gets each sprite in self.sprites() minus any classes that are "Player" or "GameObjects".
        # *(Draw MAP only)*
        for sprite in sorted([ins for ins in self.sprites() if ins.__class__ != Player and GameObjects], key = lambda a: a.zed):
            # creates offset vairable that takes the current rect position and subtracts offset from it
            offset = sprite.rect.center - self.offset
            # blits each of the sprites to the screen as offset positioning
            screen.blit(sprite.image, offset)

        # Gets each sprite in self.sprites() that are equal to class GameObjects
        for sprite in sorted([ins for ins in self.sprites() if ins.__class__ == GameObjects], key= lambda a: a.rect.y):
            # Pass for now
            pass

        # Gets each sprite in self.sprites() that are equal to class Player
        for sprite in [ins for ins in self.sprites() if ins.__class__ == Player]:
            # creates offset vairable that takes the current rect position and subtracts offset from it
            offset = sprite.rect.topleft - self.offset
            # blits each of the sprites to the screen as offset positioning
            screen.blit(sprite.image, offset)
            # blits each of the sprites shadow to the screen as offset positioning
            screen.blit(sprite.__getattribute__('shadow'), offset)
            # blits each of the sprites light to the screen as offset positioning
            screen.blit(sprite.__getattribute__('light'), offset)

    def update(self, screen, dt):
        for sprite in [ins for ins in self.sprites() if ins.__class__ == Player]:
            sprite.update(screen, dt)

    # Prints all sprites present in
    def get_all(self):
        for sprite in sorted(self.sprites(), key = lambda a: a.zed):
            print(sprite)