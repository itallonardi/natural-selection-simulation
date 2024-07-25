import pygame
from constants import TERRAIN, TERRAIN_COLORS, WIDTH, HEIGHT


def draw_terrain(screen):
    for y in range(HEIGHT // 10):
        for x in range(WIDTH // 10):
            rect = pygame.Rect(x * 10, y * 10, 10, 10)
            terrain_type = TERRAIN[y][x]
            pygame.draw.rect(screen, TERRAIN_COLORS[terrain_type], rect)
