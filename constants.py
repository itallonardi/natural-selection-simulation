import pygame
import sys
import time
import random
from constants import WIDTH, HEIGHT, PANEL_WIDTH, BACKGROUND_COLOR, FPS, INITIAL_POPULATION, FOOD_APPEAR_INTERVAL, DEATH_ANIMATION_DURATION, record_highs, record_lows
from terrain import draw_terrain
from organism import Organism
from utils import create_food
from assets.font import load_font


def draw_panel(screen, font, organism_count, food_count):
    panel_x = WIDTH
    pygame.draw.rect(screen, (50, 50, 50), (panel_x, 0, PANEL_WIDTH, HEIGHT))

    text_lines = [
        "Record Highs:",
        f"Speed: {record_highs['speed']:.2f}",
        f"Size: {record_highs['size']:.2f}",
        f"Energy Efficiency: {record_highs['energy_efficiency']:.2f}",
        f"Escape Ability: {record_highs['escape_ability']:.2f}",
        f"Recovery Ability: {record_highs['recovery_ability']:.2f}",
        f"Life Time: {record_highs['life_time']:.2f}",
        f"Organisms: {record_highs['max_organisms']}",
        f"Food: {record_highs['max_food']}",
        "",
        "Record Lows:",
        f"Speed: {record_lows['speed']:.2f}",
        f"Size: {record_lows['size']:.2f}",
        f"Energy Efficiency: {record_lows['energy_efficiency']:.2f}",
        f"Escape Ability: {record_lows['escape_ability']:.2f}",
        f"Recovery Ability: {record_lows['recovery_ability']:.2f}",
        f"Life Time: {record_lows['life_time']:.2f}",
        "",
        "Current Stats:",
        f"Current Organisms: {organism_count}",
        f"Current Food: {food_count}"
    ]

    for i, line in enumerate(text_lines):
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (panel_x + 10, 10 + i * 20))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH + PANEL_WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = load_font()

    organisms = [Organism(random.randint(0, WIDTH), random.randint(
        0, HEIGHT), 2, 5, 0.5, 0.5, 0.1) for _ in range(INITIAL_POPULATION)]
    food_sources = [create_food() for _ in range(10)]
    last_food_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_terrain(screen)

        current_time = pygame.time.get_ticks()
        if current_time - last_food_time > FOOD_APPEAR_INTERVAL:
            food_sources.append(create_food())
            last_food_time = current_time

        new_organisms = []
        for organism in organisms:
            if organism.dead:
                if time.time() - organism.death_start_time > DEATH_ANIMATION_DURATION:
                    continue  # Skip dead organism after death animation
            else:
                organism.move(food_sources)
                organism.recover()
                if organism.energy <= 0 or organism.health <= 0:
                    organism.die()
                    continue
                for food in food_sources:
                    if abs(organism.x - food[0]) < 5 and abs(organism.y - food[1]) < 5:
                        organism.eat()
                        food_sources.remove(food)
                        break
                offspring = organism.reproduce()
                if offspring:
                    new_organisms.append(offspring)
            new_organisms.append(organism)

        organisms = new_organisms
        organism_count = len(organisms)
        food_count = len(food_sources)

        record_highs['max_organisms'] = max(
            record_highs['max_organisms'], organism_count)
        record_highs['max_food'] = max(record_highs['max_food'], food_count)

        for organism in organisms:
            organism.draw(screen, font)

        for food in food_sources:
            pygame.draw.circle(screen, (255, 0, 0), food, 3)

        draw_panel(screen, font, organism_count, food_count)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
