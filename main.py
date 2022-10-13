import pygame
import sys
import game
from settings.window import WINDOW_W, WINDOW_H
from map import konoha
from settings import tile_size

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
clock = pygame.time.Clock()
pygame.display.set_caption("Project Shinobi")

game = game.Game()

for row_index, row in enumerate(konoha.world):
    for column_index, column in enumerate(row):
        print(f"x: {row_index * tile_size.tile_size}, y: {column_index * tile_size.tile_size}")


while True:
    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            sys.exit()
    dt = clock.tick() / 1000

    screen.fill((20, 20, 20))

    game.update(screen, dt)

    pygame.display.update()


