import math
import pygame
import pygame.gfxdraw
import random


def draw_star(screen, x, y, size, color):
    points = []
    for i in range(30):  # 10 points, for example, for a 5-point star
        angle = i * math.pi / 12
        radius = size if i % 2 == 0 else size / 2
        point_x = x + radius * math.cos(angle)
        point_y = y + radius * math.sin(angle)
        points.append((int(point_x), int(point_y)))
    pygame.gfxdraw.filled_polygon(screen, points, color)
    pygame.gfxdraw.aapolygon(screen, points, color)


def create_food():
    from constants import WIDTH, HEIGHT
    return (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
